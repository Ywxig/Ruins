
//  RUINS — PageLoader.js (рефакторинг)


const DEBUG = true;
const lastFloor = localStorage.getItem("lastFloor") || 1;
//  Настройки 
const BLOCK_SIZE = 32;
const MAP_W = 16;
const MAP_H = 12;
const CANVAS_COLS = 19;   // сколько клеток видно по горизонтали
const CANVAS_ROWS = 13;   // сколько клеток видно по вертикали

//  Описание тайлов 
const TILES = {
    "hero": { 
        color: "#2a2a3a", 
        type: "player", 
        symbolColor: "#66ccff",  // голубой герой
        char: "@" 
    },
    "0": { 
        color: "#111111", 
        type: "wall", 
        symbolColor: "#333333",
        char: ""                 // решётка для стен
    },
    "1": { 
        color: "#1a1a1a", 
        type: "floor", 
        symbolColor: "#2a2a2a",
        char: "" 
    },
    "e": { 
        color: "#3a1a1a", 
        type: "enemy", 
        symbolColor: "#ff3333",   // красный враг
        char: "☠" 
    },
    "E": { 
        color: "#1a3a1a", 
        type: "exit", 
        symbolColor: "#33ff33",   // зелёный выход
        char: "⬇" 
    },
    "H": { 
        color: "#3a1a3a", 
        type: "health", 
        symbolColor: "#ff66cc",   // розовый хил
        char: "❤" 
    }
};

const WALKABLE = new Set(["1", "e", "E", "H"]);

//  Состояние игры 
let map        = [];
let playerPos  = { x: 0, y: 0 };
let floorNum   = 1;
let player     = { hp: 100, maxHp: 100, attack: 20 };
let enemyDmg   = 15;   // урон от каждого врага при наступании

//  Утилиты 
function log(msg) { if (DEBUG) console.log(msg); }

function randInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function showEvent(msg) {
    const el = document.getElementById("event-log");
    if (!el) return;
    el.innerHTML = `<span>${msg}</span>`;
}

//  Генерация подземелья 
function generateDungeon(w, h) {
    const steps = Math.round((w * h) / 2.5);
    const grid  = Array.from({ length: h }, () => Array(w).fill("0"));

    let x = 1, y = 1;
    grid[y][x] = "1";

    for (let i = 0; i < steps; i++) {
        const d = randInt(0, 3);
        if (d === 0 && x + 1 < w - 1) x++;
        else if (d === 1 && x - 1 > 0) x--;
        else if (d === 2 && y + 1 < h - 1) y++;
        else if (d === 3 && y - 1 > 0) y--;
        grid[y][x] = "1";
    }

    // Враги
    const enemyCount = Math.floor((w * h) / 18);
    for (let i = 0; i < enemyCount; i++) {
        const ex = randInt(1, w - 2);
        const ey = randInt(1, h - 2);
        if (grid[ey][ex] === "1") grid[ey][ex] = "e";
    }

    // Хилка
    const healthCount = Math.floor((w * h) / 30);
    for (let i = 0; i < healthCount; i++) {
        const hx = randInt(1, w - 2);
        const hy = randInt(1, h - 2);
        if (grid[hy][hx] === "1") grid[hy][hx] = "H";
    }

    // Выход — последняя обработанная клетка
    grid[y][x] = "E";

    return grid;
}

//  Рендер 
function render() {
    const canvas = document.getElementById("canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    ctx.fillStyle = "#050508";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Смещение камеры (центрируем игрока)
    const camOffX = Math.floor(CANVAS_COLS / 2) - playerPos.x;
    const camOffY = Math.floor(CANVAS_ROWS / 2) - playerPos.y;

    for (let row = 0; row < map.length; row++) {
        for (let col = 0; col < map[row].length; col++) {
            const tile = map[row][col];
            const sx   = (col + camOffX) * BLOCK_SIZE;
            const sy   = (row + camOffY) * BLOCK_SIZE;

            if (sx < -BLOCK_SIZE || sy < -BLOCK_SIZE ||
                sx > canvas.width + BLOCK_SIZE || sy > canvas.height + BLOCK_SIZE) continue;

            const info = TILES[tile];
            if (!info) continue;

            ctx.fillStyle = info.color;
            ctx.fillRect(sx, sy, BLOCK_SIZE, BLOCK_SIZE);

            // Символы поверх плитки
            if (info.char) {
                ctx.fillStyle = TILES[tile].color;
                ctx.font = `${BLOCK_SIZE - 4}px monospace`;
                ctx.textAlign = "center";
                ctx.textBaseline = "middle";
                ctx.fillStyle = TILES[tile].symbolColor || "#FFFFFF"; // используем цвет символа из конфига
                ctx.fillText(TILES[tile].char, sx + BLOCK_SIZE / 2, sy + BLOCK_SIZE / 2);
            }
        }
    }
    

    // Игрок
    const px = (playerPos.x + camOffX) * BLOCK_SIZE;
    const py = (playerPos.y + camOffY) * BLOCK_SIZE;
    ctx.fillStyle = TILES["hero"].color;
    ctx.fillRect(px + 2, py + 2, BLOCK_SIZE - 4, BLOCK_SIZE - 4);
    ctx.fillStyle = TILES["hero"].symbolColor || "#cc99ff";
    ctx.font = `${BLOCK_SIZE - 6}px monospace`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(TILES["hero"].char, px + BLOCK_SIZE / 2, py + BLOCK_SIZE / 2);

    updateHUD();
}

function updateHUD() {
    const hpBar  = document.getElementById("hp-bar");
    const hpText = document.getElementById("hp-text");
    const flTxt  = document.getElementById("floor-text");
    const lastFloor = localStorage.getItem("lastFloor") || 1;
    if (hpBar)  hpBar.style.width  = Math.max(0, (player.hp / player.maxHp) * 100) + "%";
    if (hpText) hpText.textContent = `${player.hp} / ${player.maxHp}`;
    if (flTxt)  flTxt.textContent  = `Этаж ${floorNum}/${lastFloor}`;
    eventLog = document.getElementById("event-log");
    eventLog.style.width = `${CANVAS_COLS * BLOCK_SIZE + 4}px`;
}

//  Движение и мгновенный бой 
function move(dir) {
    let nx = playerPos.x;
    let ny = playerPos.y;

    if (dir === "up")    ny--;
    if (dir === "down")  ny++;
    if (dir === "left")  nx--;
    if (dir === "right") nx++;

    // Граница карты
    if (nx < 0 || ny < 0 || ny >= map.length || nx >= map[0].length) return;

    const tile = map[ny][nx];

    if (!WALKABLE.has(tile)) return; // стена

    //  Мгновенный бой 
    if (tile === "e") {
        player.hp -= enemyDmg;
        map[ny][nx] = "1";   // враг погибает — клетка становится полом
        showEvent(`⚔ Ты атакуешь врага! Получаешь ${enemyDmg} урона. HP: ${player.hp}`);
        log(`Бой: игрок −${enemyDmg} HP → ${player.hp}`);

        if (player.hp <= 0) {
            loadPage("death");
            return;
        }

        playerPos.x = nx;
        playerPos.y = ny;
        render();
        return;
    }

    // подбираем хилку
    if (tile === "H") {
        player.hp = Math.min(player.maxHp, player.hp + 30);
        map[ny][nx] = "1";   // клетка становится полом
        showEvent(`✨ Ты подбираешь зелье и восстанавливаешь 30 HP! HP: ${player.hp}`);
        log(`Хилка: игрок +30 HP → ${player.hp}`);

        playerPos.x = nx;
        playerPos.y = ny;
        render();
        return;
    }

    //  Выход на следующий этаж 
    if (tile === "E") {
        floorNum++;
        if (floorNum > lastFloor) {
            localStorage.setItem("lastFloor", floorNum);
        }
        showEvent(`✦ Ты спускаешься на этаж ${floorNum}…`);
        startGame();
        return;
    }

    playerPos.x = nx;
    playerPos.y = ny;
    render();
}

//  Управление с клавиатуры 
function setupKeyboard() {
    document.onkeydown = (e) => {
        const dirs = { ArrowUp: "up", ArrowDown: "down", ArrowLeft: "left", ArrowRight: "right",
                       w: "up", s: "down", a: "left", d: "right" };
        if (dirs[e.key]) { e.preventDefault(); move(dirs[e.key]); }
    };
}

//  Страницы 
function loadPage(page) {
    const content = document.getElementById("content");
    log(`[page: ${page}]`);

    switch (page) {
        case "home":
            content.innerHTML = pagHome();
            break;
        case "game":
            content.innerHTML = pageGame();
            setupKeyboard();
            startGame();
            break;
        case "death":
            content.innerHTML = pageDeath();
            document.onkeydown = null;
            break;
        default:
            content.innerHTML = `<h2>Страница не найдена</h2>`;
    }
}

function startGame() {
    map = generateDungeon(MAP_W, MAP_H);
    playerPos = { x: 1, y: 1 };
    // Убеждаемся что стартовая клетка — пол
    map[1][1] = "1";
    render();
}

//  HTML страниц 
function pagHome() {
    return `
    <div class="main-menu">
        <h1>RUINS</h1>
        <p>⚔ dungeon crawler ⚔</p>
        <button class="menu-btn" onclick="loadPage('game')">▶ Новая игра</button>
    </div>`;
}

function pageGame() {
    return `
    <div id="game-wrapper">
        <div id="hud">
            <div id="hud-left">
                <span class="hud-label">HP</span>
                <div id="hp-bar-wrap"><div id="hp-bar" style="width:100%"></div></div>
                <span id="hp-text">100 / 100</span>
            </div>
            <span id="floor-text">Этаж 1</span>
        </div>
        <canvas id="canvas"
            width="${CANVAS_COLS * BLOCK_SIZE}"
            height="${CANVAS_ROWS * BLOCK_SIZE}">
        </canvas>
        <div id="event-log"></div>
    </div>`;
}

function pageDeath() {
    return `
    <div id="death-screen" style="display:block">
        <h1>ТЫ ПОГИБ</h1>
        <p>Этаж ${floorNum} · Здоровье исчерпано</p>
        <button class="menu-btn" onclick="floorNum=1; player={hp:100,maxHp:100,attack:20}; loadPage('game')">
            ↺ Начать заново
        </button>
    </div>`;
}
