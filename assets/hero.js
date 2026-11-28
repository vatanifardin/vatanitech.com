// The hero "sculpture": a few thousand points of light that gather into
// the Vatani Tech mark, a slowly turning Earth (real coastlines, from
// PetroGram's own map), an oil drop and, on the pages of other apps, a
// cluster of crystals or a protractor on a ruler. Plain canvas, no libraries.
// It pauses off screen and stays still for people who prefer less motion.
(function () {
  const cv = document.getElementById('sculpture');
  if (!cv) return;
  const ctx = cv.getContext('2d');
  const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const names = (cv.dataset.shapes || 'mark,globe,drop').split(',');
  const cap = document.getElementById('sculpture-cap');
  const LAND = window.VL_LAND || [];

  // A small repeatable random generator, so the shapes look the same each visit.
  let seed = 20261121;
  const rnd = () => {
    seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };

  const small = Math.min(window.innerWidth, window.innerHeight) < 700;
  const stride = small ? 2 : 1;
  const L = names.includes('globe') ? Math.floor(LAND.length / 2 / stride) : (small ? 1300 : 2400);
  const A = small ? 260 : 460;          // "ambient" points: ring, dust, ripples
  const N = L + A;

  // Each shape: positions (x, y, z), colour (0 white .. 1 teal), brightness, size.
  function blank() {
    return { p: new Float32Array(N * 3), c: new Float32Array(N), a: new Float32Array(N), s: new Float32Array(N) };
  }
  function set(sh, i, x, y, z, c, a, s) {
    sh.p[i * 3] = x; sh.p[i * 3 + 1] = y; sh.p[i * 3 + 2] = z;
    sh.c[i] = c; sh.a[i] = a; sh.s[i] = s;
  }

  function makeMark() {
    const sh = blank();
    // The logo's two strokes, in its own 120 x 100 drawing units.
    const segs = [
      [15, 15, 60, 85, 11, 0], [60, 85, 105, 15, 11, 0],
      [35, 15, 60, 55, 9, 1], [60, 55, 85, 15, 9, 1],
    ];
    const weight = segs.map((s) => Math.hypot(s[2] - s[0], s[3] - s[1]) * s[4]);
    const total = weight.reduce((x, y) => x + y, 0);
    let i = 0;
    segs.forEach((s, k) => {
      const n = k === segs.length - 1 ? L - i : Math.round(L * weight[k] / total);
      const dx = s[2] - s[0], dy = s[3] - s[1], len = Math.hypot(dx, dy);
      const nx = -dy / len, ny = dx / len;
      for (let j = 0; j < n && i < L; j++, i++) {
        const t = rnd(), off = (rnd() - 0.5) * s[4];
        const px = s[0] + dx * t + nx * off, py = s[1] + dy * t + ny * off;
        set(sh, i, (px - 60) / 44, -(py - 50) / 44, (rnd() - 0.5) * 0.16,
          s[5] ? 1 : 0, 1, 1.12);
      }
    });
    for (; i < N; i++) {                 // dust drifting around the mark
      const r = 1.5 + rnd() * 0.9, u = rnd() * 2 - 1, th = rnd() * 6.283;
      const q = Math.sqrt(1 - u * u);
      set(sh, i, r * q * Math.cos(th), r * u * 0.8, r * q * Math.sin(th), rnd() < 0.3 ? 1 : 0, 0.28, 0.8);
    }
    return sh;
  }

  function makeGlobe() {
    const sh = blank();
    for (let i = 0; i < L; i++) {
      const lon = LAND[i * stride * 2] / 10 * Math.PI / 180;
      const lat = LAND[i * stride * 2 + 1] / 10 * Math.PI / 180;
      const hot = rnd() < 0.035;         // a few bright teal points
      set(sh, i, Math.cos(lat) * Math.sin(lon), Math.sin(lat), Math.cos(lat) * Math.cos(lon),
        hot ? 1 : 0.12, hot ? 1 : 0.9, hot ? 2.1 : 1);
    }
    for (let i = L; i < N; i++) {        // a thin ring around the Earth
      const th = (i - L) / A * 6.283, r = 1.42 + (rnd() - 0.5) * 0.05;
      set(sh, i, r * Math.cos(th), (rnd() - 0.5) * 0.02, r * Math.sin(th), 1, 0.5, 0.8);
    }
    return sh;
  }

  function makeDrop() {
    const sh = blank();
    for (let i = 0; i < L; i++) {
      const u = rnd(), t = Math.PI * Math.pow(u, 0.82), ph = rnd() * 6.283;
      const r = 1.18 * Math.sin(t) * Math.pow(Math.sin(t / 2), 1.5);
      set(sh, i, r * Math.cos(ph), 1.12 * Math.cos(t) + 0.12, r * Math.sin(ph),
        0.35 + 0.65 * u, 0.9, 1);
    }
    for (let i = L; i < N; i++) {        // ripples under the drop
      const ring = (i - L) % 4, th = rnd() * 6.283, r = 0.5 + ring * 0.33 + (rnd() - 0.5) * 0.03;
      set(sh, i, r * Math.cos(th), -1.2, r * Math.sin(th), 1, 0.9 - ring * 0.17, 0.9);
    }
    return sh;
  }

  function makeNebula() {
    const sh = blank();
    for (let i = 0; i < N; i++) {
      const r = 1.2 + rnd() * 2.6, u = rnd() * 2 - 1, th = rnd() * 6.283, q = Math.sqrt(1 - u * u);
      set(sh, i, r * q * Math.cos(th), r * u, r * q * Math.sin(th), rnd() < 0.4 ? 1 : 0, 0.25, 0.8);
    }
    return sh;
  }

  // A cluster of crystals (OreGram): six-sided columns with pointed tips.
  function makeCrystal() {
    const sh = blank();
    // each: foot (x, z), radius, height of the column, height of the tip, lean (z, x)
    const cols = [[0, 0, 0.36, 1.25, 0.5, 0, 0], [-0.5, 0.12, 0.25, 0.7, 0.36, 0.5, 0.12], [0.46, -0.1, 0.27, 0.82, 0.38, -0.42, -0.16],
      [0.12, 0.42, 0.2, 0.46, 0.3, -0.12, 0.55], [-0.2, -0.42, 0.18, 0.4, 0.28, 0.2, -0.5]];
    const share = [0.42, 0.18, 0.2, 0.1, 0.1];
    let i = 0;
    cols.forEach((c, k) => {
      const n = k === cols.length - 1 ? L - i : Math.round(L * share[k]);
      const cz = Math.cos(c[5]), sz = Math.sin(c[5]), cx2 = Math.cos(c[6]), sx = Math.sin(c[6]);
      for (let j = 0; j < n && i < L; j++, i++) {
        const side = Math.floor(rnd() * 6), a0 = side * 1.0472, a1 = a0 + 1.0472;
        const edge = rnd() < 0.5;                 // half of the points sit on the edges, so the facets read
        let f = edge ? (rnd() < 0.5 ? 0 : 1) : rnd(), x, y, z, tip = rnd() < 0.3;
        const bx = Math.cos(a0) + (Math.cos(a1) - Math.cos(a0)) * f, bz = Math.sin(a0) + (Math.sin(a1) - Math.sin(a0)) * f;
        if (tip) { const v = edge && rnd() < 0.3 ? 0 : rnd(); x = bx * c[2] * (1 - v); z = bz * c[2] * (1 - v); y = c[3] + c[4] * v; }
        else { x = bx * c[2]; z = bz * c[2]; y = (edge && rnd() < 0.25 ? 1 : rnd()) * c[3]; }
        const x1 = x * cz - y * sz, y1 = x * sz + y * cz;        // lean the column
        const y2 = y1 * cx2 - z * sx, z2 = y1 * sx + z * cx2;
        const hot = rnd() < 0.03;
        set(sh, i, x1 + c[0], y2 - 0.85, z2 + c[1], hot ? 1 : (edge ? 0.75 : 0.3 + 0.4 * (y / (c[3] + c[4]))), hot ? 1 : (edge ? 0.95 : 0.6), hot ? 2 : 1);
      }
    });
    for (; i < N; i++) {                   // the ground the crystals grow from
      const th = rnd() * 6.283, r = Math.sqrt(rnd()) * 1.25;
      set(sh, i, r * Math.cos(th), -0.87 + (rnd() - 0.5) * 0.05, r * Math.sin(th), rnd() < 0.5 ? 1 : 0.2, 0.75 - r * 0.4, 0.85);
    }
    return sh;
  }

  // A protractor on a ruler, with a needle (Geo-Rulers).
  function makeTools() {
    const sh = blank();
    const deg = Math.PI / 180, NA = 52 * deg, oy = -0.5;
    for (let i = 0; i < L; i++) {
      const u = rnd(), zz = (rnd() - 0.5) * 0.08;
      let x, y, c = 0.25, a = 0.85, s = 1;
      if (u < 0.24) {                       // the outer arc
        const th = rnd() * Math.PI, r = 1.18 + (rnd() - 0.5) * 0.035; x = r * Math.cos(th); y = r * Math.sin(th);
      } else if (u < 0.34) {                // the inner arc
        const th = rnd() * Math.PI, r = 0.42 + (rnd() - 0.5) * 0.02; x = r * Math.cos(th); y = r * Math.sin(th); a = 0.6;
      } else if (u < 0.56) {                // degree marks, longer every 30 degrees
        const k = Math.floor(rnd() * 19), th = k * 10 * deg, r = 1.16 - rnd() * (k % 3 === 0 ? 0.26 : 0.12);
        x = r * Math.cos(th); y = r * Math.sin(th); c = 0.6;
      } else if (u < 0.86) {                // the ruler under it: outline and marks
        const v = rnd();
        if (v < 0.45) { x = (rnd() * 2 - 1) * 1.32; y = rnd() < 0.5 ? -0.03 : -0.34; }
        else if (v < 0.52) { x = rnd() < 0.5 ? -1.32 : 1.32; y = -0.03 - rnd() * 0.31; }
        else { const k = Math.floor(rnd() * 25); x = -1.2 + k * 0.1; y = -0.03 - rnd() * (k % 5 === 0 ? 0.2 : 0.1); c = 0.6; }
      } else {                              // the needle, in the accent colour
        const r = rnd() * 1.1; x = r * Math.cos(NA) + (rnd() - 0.5) * 0.02; y = r * Math.sin(NA) + (rnd() - 0.5) * 0.02;
        c = 1; a = 1; s = r > 1.04 ? 2.1 : 1.1;
      }
      set(sh, i, x, y + oy, zz, c, a, s);
    }
    for (let i = L; i < N; i++) {          // dust drifting around
      const r = 1.6 + rnd() * 0.9, u = rnd() * 2 - 1, th = rnd() * 6.283, q = Math.sqrt(1 - u * u);
      set(sh, i, r * q * Math.cos(th), r * u * 0.8, r * q * Math.sin(th), rnd() < 0.3 ? 1 : 0, 0.26, 0.8);
    }
    return sh;
  }

  // An anchor over rings of water (MarineGram).
  function makeAnchor() {
    const sh = blank();
    for (let i = 0; i < L; i++) {
      const u = rnd(), zz = (rnd() - 0.5) * 0.12, w = (rnd() - 0.5) * 0.09;
      let x, y, c = 0.3, a = 0.9, s = 1;
      if (u < 0.1) {                         // the ring at the top
        const th = rnd() * 6.283, r = 0.17 + w * 0.6; x = r * Math.cos(th); y = 1.05 + r * Math.sin(th); c = 0.85;
      } else if (u < 0.34) {                 // the shank
        x = w; y = -1.05 + rnd() * 1.93;
      } else if (u < 0.46) {                 // the stock (cross bar)
        x = (rnd() * 2 - 1) * 0.5; y = 0.62 + w * 0.8;
      } else if (u < 0.8) {                  // the two arms: an arc
        const th = (200 + rnd() * 140) * Math.PI / 180, r = 0.8 + w; x = r * Math.cos(th); y = -0.25 + r * Math.sin(th);
      } else {                               // the flukes: a triangle at each end
        let p = rnd(), q = rnd(); if (p + q > 1) { p = 1 - p; q = 1 - q; }
        const sgn = u < 0.9 ? -1 : 1;
        x = sgn * (0.93 + p * (0.55 - 0.93) + q * (0.86 - 0.93)); y = -0.18 + p * (-0.44 + 0.18) + q * (-0.7 + 0.18);
        c = 0.9; a = 1;
      }
      set(sh, i, x, y + 0.08, zz, c, a, s);
    }
    for (let i = L; i < N; i++) {           // rings of water under it
      const ring = (i - L) % 4, th = rnd() * 6.283, r = 0.55 + ring * 0.34 + (rnd() - 0.5) * 0.03;
      set(sh, i, r * Math.cos(th), -1.15, r * Math.sin(th), 1, 0.85 - ring * 0.16, 0.9);
    }
    return sh;
  }

  // A pointed arch with a crescent and an open book (Quran Guardians).
  function makeArch() {
    const sh = blank();
    const arch = (hw, t) => {                // a point of a pointed arch of half-width hw, t in 0..1
      const side = t < 0.5 ? -1 : 1, v = t < 0.5 ? t * 2 : (1 - t) * 2, th = (180 - 60 * v) * Math.PI / 180;
      return [side * -(hw + 2 * hw * Math.cos(th)), -0.1 + 2 * hw * Math.sin(th)];
    };
    for (let i = 0; i < L; i++) {
      const u = rnd(), j = (rnd() - 0.5) * 0.025;
      let x, y, z = (rnd() - 0.5) * 0.05, c = 0.25, a = 0.9, s = 1;
      if (u < 0.3) { const q = arch(0.8, rnd()); x = q[0] + j; y = q[1] + j; z += 0.1; }
      else if (u < 0.5) { const q = arch(0.62, rnd()); x = q[0] + j; y = q[1] + j; z -= 0.1; a = 0.7; }
      else if (u < 0.68) {                   // the pillars and the floor
        const v = rnd();
        if (v < 0.36) { x = (rnd() < 0.5 ? -0.8 : 0.8) + j; y = -1.1 + rnd(); z += 0.1; }
        else if (v < 0.64) { x = (rnd() < 0.5 ? -0.62 : 0.62) + j; y = -1.1 + rnd(); z -= 0.1; a = 0.7; }
        else { x = (rnd() * 2 - 1) * (rnd() < 0.5 ? 0.98 : 1.08); y = rnd() < 0.5 ? -1.1 : -1.18; }
      } else if (u < 0.78) {                 // the crescent
        do { const th = rnd() * 6.283, r = Math.sqrt(rnd()) * 0.17; x = r * Math.cos(th); y = 0.66 + r * Math.sin(th); }
        while (Math.hypot(x - 0.075, y - 0.69) < 0.15);
        c = 1; a = 1;
      } else {                               // the open book: two pages with lines
        const sgn = rnd() < 0.5 ? -1 : 1, v = rnd(), k = rnd();
        const row = v < 0.5 ? (rnd() < 0.5 ? 0 : 1) : (1 + Math.floor(rnd() * 4)) / 6;   // edges, or a line of writing
        const kk = v < 0.5 ? k : 0.14 + k * 0.72;
        x = sgn * kk * 0.46; y = -0.5 - row * 0.3 + kk * 0.1 - 0.02;
        if (v < 0.12) { x = sgn * 0.46; y = -0.42 - rnd() * 0.3; }
        c = 1; a = v < 0.5 ? 1 : 0.75;
      }
      set(sh, i, x, y + 0.12, z, c, a, s);
    }
    for (let i = L; i < N; i++) {           // stars around it
      const r = 1.5 + rnd() * 1.0, u = rnd() * 2 - 1, th = rnd() * 6.283, q = Math.sqrt(1 - u * u), hot = rnd() < 0.06;
      set(sh, i, r * q * Math.cos(th), r * u * 0.85, r * q * Math.sin(th), hot ? 1 : 0, hot ? 0.9 : 0.26, hot ? 1.7 : 0.8);
    }
    return sh;
  }

  const makers = { mark: makeMark, globe: makeGlobe, drop: makeDrop, crystal: makeCrystal, tools: makeTools, anchor: makeAnchor, arch: makeArch };
  const spin = {                          // how each shape turns: [y, z, x] angles
    mark: (t) => [Math.sin(t * 0.45) * 0.42, 0, Math.sin(t * 0.31) * 0.07],
    // The Earth starts facing the Caspian and turns toward the Atlantic.
    globe: (t, local) => [-1.25 + local * 0.2, 0.3, 0.2],
    drop: (t) => [t * 0.42, 0, 0.16],
    crystal: (t) => [t * 0.36, 0, 0.2],
    anchor: (t) => [Math.sin(t * 0.38) * 0.75, Math.sin(t * 0.5) * 0.05, 0.14],
    arch: (t) => [Math.sin(t * 0.33) * 0.42, 0, 0.05 + Math.sin(t * 0.27) * 0.05],
    tools: (t) => [Math.sin(t * 0.4) * 0.5, Math.sin(t * 0.27) * 0.05, 0.1 + Math.sin(t * 0.31) * 0.08],
    nebula: (t) => [t * 0.1, 0, 0.2],
  };
  const hold = { mark: 4.6, globe: 9, drop: 5.2, crystal: 8, tools: 8, anchor: 8, arch: 8 };
  // Captions: number, text and, where given, the language of the text. The
  // page hands them over in its own language (see build.py).
  let captions = {
    mark: ['01', 'Vatani Tech', 'en'],
    globe: ['02', 'Anywhere on Earth, offline'],
    drop: ['03', 'PetroGram · oil & gas'],
  };
  try { captions = JSON.parse(cv.dataset.captions) || captions; } catch (e) { /* keep the English ones */ }
  const shapes = names.map((n) => ({ name: n, data: makers[n]() }));
  const nebula = { name: 'nebula', data: makeNebula() };

  // Per-point timing and a sideways swing, so points flow instead of sliding.
  const delay = new Float32Array(N), swing = new Float32Array(N * 3);
  for (let i = 0; i < N; i++) {
    delay[i] = rnd() * 0.38;
    swing[i * 3] = rnd() - 0.5; swing[i * 3 + 1] = rnd() - 0.5; swing[i * 3 + 2] = rnd() - 0.5;
  }

  // Colour table: 6 tints x 12 brightness steps (no text is built per point).
  // The page's accent colour (teal; an app's page may set its own in --acc).
  const ACC = (getComputedStyle(document.body).getPropertyValue('--acc') || '').split(',').map(Number);
  const tint = ACC.length === 3 && ACC.every((n) => n >= 0) && ACC.join() !== '44,196,184' ? ACC : [44, 212, 200];
  const TINTS = 6, STEPS = 12, table = [];
  for (let c = 0; c < TINTS; c++) {
    const k = c / (TINTS - 1);
    const r = Math.round(226 + (tint[0] - 226) * k), g = Math.round(233 + (tint[1] - 233) * k), b = Math.round(255 + (tint[2] - 255) * k);
    table.push(Array.from({ length: STEPS + 1 }, (_, a) => `rgba(${r},${g},${b},${(a / STEPS).toFixed(3)})`));
  }

  let w = 0, h = 0, cx = 0, cy = 0, R = 0;
  function resize() {
    w = cv.clientWidth; h = cv.clientHeight;
    // Sharp on good screens, but never more pixels than a modest computer can paint smoothly.
    const dpr = Math.max(1, Math.min(window.devicePixelRatio || 1, 2, Math.sqrt(2.2e6 / Math.max(1, w * h))));
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cx = w * 0.5; cy = h * 0.5;
    R = Math.min(w, h) * 0.3;
  }

  let from = nebula, to = shapes[0], idx = 0, phase = 'morph', clock = 0, t = 0;
  const entered = { nebula: 0 }; entered[to.name] = 0;   // when each shape last began to form
  const MORPH = 2.6;
  let mx = 0, my = 0, tx = 0, ty = 0;      // pointer tilt (eased)
  const ease = (x) => x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
  const tmp = [0, 0, 0];

  function turn(p, i, ang) {              // rotate point i of p by [y, z, x]
    const x = p[i * 3], y = p[i * 3 + 1], z = p[i * 3 + 2];
    let c = Math.cos(ang[0]), s = Math.sin(ang[0]);
    const x1 = x * c + z * s, z1 = -x * s + z * c;
    c = Math.cos(ang[1]); s = Math.sin(ang[1]);
    const x2 = x1 * c - y * s, y2 = x1 * s + y * c;
    c = Math.cos(ang[2]); s = Math.sin(ang[2]);
    tmp[0] = x2; tmp[1] = y2 * c - z1 * s; tmp[2] = y2 * s + z1 * c;
  }

  function setCaption(name) {
    if (!cap || !captions[name]) return;
    cap.classList.remove('on');
    setTimeout(() => {
      const num = document.createElement('b'), text = document.createElement('span');
      num.textContent = captions[name][0];
      text.textContent = captions[name][1];
      if (captions[name][2]) text.lang = captions[name][2];
      cap.replaceChildren(num, ' ', text);
      cap.classList.add('on');
    }, 350);
  }

  function frame(dt) {
    t += dt; clock += dt;
    if (phase === 'morph' && clock >= MORPH) {
      phase = 'hold'; clock = 0; from = to;
    } else if (phase === 'hold' && shapes.length > 1 && clock >= hold[to.name]) {
      phase = 'morph'; clock = 0; idx = (idx + 1) % shapes.length; to = shapes[idx]; entered[to.name] = t;
      setCaption(to.name);
    }
    const P = phase === 'morph' ? clock / MORPH : 1;
    mx += (tx - mx) * 0.05; my += (ty - my) * 0.05;
    const aTo = spin[to.name](t, t - entered[to.name]), aFrom = spin[from.name](t, t - entered[from.name]);
    aTo[0] += mx * 0.5; aTo[2] += my * 0.3; aFrom[0] += mx * 0.5; aFrom[2] += my * 0.3;
    const A0 = from.data, B0 = to.data, D = 3.6;
    const pulse = 0.75 + 0.25 * Math.sin(t * 2.4);

    ctx.clearRect(0, 0, w, h);
    // A soft "atmosphere" behind the Earth, so the oceans read as a sphere.
    const g = to.name === 'globe' ? (P < 1 ? ease(P) : 1) : (from.name === 'globe' && P < 1 ? 1 - ease(P) : 0);
    if (g > 0.01) {
      const rr = R * 1.02;
      const grad = ctx.createRadialGradient(cx - rr * 0.3, cy - rr * 0.35, rr * 0.1, cx, cy, rr);
      grad.addColorStop(0, `rgba(70,110,220,${0.2 * g})`);
      grad.addColorStop(0.7, `rgba(30,50,130,${0.14 * g})`);
      grad.addColorStop(1, `rgba(44,196,184,${0.05 * g})`);
      ctx.globalCompositeOperation = 'source-over';
      ctx.fillStyle = grad; ctx.beginPath(); ctx.arc(cx, cy, rr, 0, 6.283); ctx.fill();
      ctx.strokeStyle = `rgba(127,240,228,${0.3 * g})`; ctx.lineWidth = 1; ctx.stroke();
    }
    ctx.globalCompositeOperation = 'lighter';
    for (let i = 0; i < N; i++) {
      let x, y, z, c, a, s;
      if (P < 1) {
        const k = ease(Math.min(1, Math.max(0, (P - delay[i]) / 0.62)));
        turn(A0.p, i, aFrom); const ax = tmp[0], ay = tmp[1], az = tmp[2];
        turn(B0.p, i, aTo);
        const arc = Math.sin(Math.PI * k) * 0.55;
        x = ax + (tmp[0] - ax) * k + swing[i * 3] * arc;
        y = ay + (tmp[1] - ay) * k + swing[i * 3 + 1] * arc;
        z = az + (tmp[2] - az) * k + swing[i * 3 + 2] * arc;
        c = A0.c[i] + (B0.c[i] - A0.c[i]) * k;
        a = A0.a[i] + (B0.a[i] - A0.a[i]) * k;
        s = A0.s[i] + (B0.s[i] - A0.s[i]) * k;
      } else {
        turn(B0.p, i, aTo); x = tmp[0]; y = tmp[1]; z = tmp[2];
        c = B0.c[i]; a = B0.a[i]; s = B0.s[i];
      }
      const f = Math.min(1, Math.max(0, (z + 1.25) / 2.5));   // 0 far .. 1 near
      const k2 = D / (D - z);
      const px = cx + x * R * k2, py = cy - y * R * k2;
      if (px < -4 || px > w + 4 || py < -4 || py > h + 4) continue;
      let alpha = a * (0.16 + 0.84 * Math.pow(f, 1.6));
      if (s > 1.5) alpha *= pulse;
      const size = (1.05 + 1.75 * f) * s * (small ? 0.85 : 1);
      ctx.fillStyle = table[Math.round(c * (TINTS - 1))][Math.round(Math.min(1, alpha) * STEPS)];
      if (size > 2.6) { ctx.beginPath(); ctx.arc(px, py, size * 0.6, 0, 6.283); ctx.fill(); }
      else ctx.fillRect(px - size / 2, py - size / 2, size, size);
    }
  }

  let visible = true, last = 0;
  function loop(now) {
    const dt = Math.min(0.05, (now - last) / 1000 || 0.016); last = now;
    if (visible && !document.hidden) frame(dt);
    requestAnimationFrame(loop);
  }

  function drawStill() {                  // one calm picture, no movement
    from = to = shapes[0]; entered[to.name] = 0; phase = 'hold'; clock = 0; t = 0.8; frame(0);
  }

  window.addEventListener('resize', () => { resize(); if (still) drawStill(); });
  window.addEventListener('pointermove', (e) => {
    tx = (e.clientX / window.innerWidth - 0.5) * 2;
    ty = (e.clientY / window.innerHeight - 0.5) * 2;
  }, { passive: true });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver((e) => { visible = e[0].isIntersecting; }).observe(cv);
  }

  resize();
  setCaption(to.name);
  if (still) drawStill(); else requestAnimationFrame(loop);
})();
