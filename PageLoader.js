
__DEBUG__ = true

block_size = 32
canvas_size = [3,3]
map_size = [10,10]
generateDungeon(map_size[0], map_size[1], Math.round((map_size[0]*map_size[1]) / 3));
let map = generateDungeon(map_size[0], map_size[1], Math.round((map_size[0]*map_size[1]) / 3));
localStorage.setItem("map", JSON.stringify(map))
localStorage.setItem("player_pos", JSON.stringify([0, 0]))

game = false

ITEMS = {
    "player" : {name: "@", color: "violet", texture: "player.png", model: "https://preview.redd.it/pixel-ellen-v0-6zjjooemeqad1.png?width=4830&format=png&auto=webp&s=e4532eca4dc9e9900b7a662a392cfd145cdc0848", type: "player"},
    "0" : {name: "0", color: "rgb(158, 158, 158)", texture: "https://img.freepik.com/free-vector/stone-wall-texture_1110-425.jpg", type: "wall"},
    "1" : {name: "1", color: "rgb(58, 58, 58)", texture: "https://godotmarketplace.com/wp-content/uploads/2023/11/3.jpg", type: "flor"},
    "[" : {name: "[", color: "rgb(58, 58, 58)", texture: "https://godotmarketplace.com/wp-content/uploads/2023/11/3.jpg", type: "flor"},
    "e" : {name: "e", color: "rgb(145, 0, 0)", texture: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4lZiy5Jvdr0UvH-kXVgbEfNnDn6cvLHg67eKT42QtK74FUg46WuO4wMg3etDJq2HAF4A&usqp=CAU", type: "enemy"},
    "E" : {name: "E", color: "rgb(1, 255, 65)", texture: "", type: "exit"} 
}

stap_blocks = ['1', "e", "E", "["]



function playBGmusic() {
    const musicPlaer = document.getElementById('musicPlayer');
    let audio = new Audio('D:\\Music\\AC-DC\\2020 - Power Up\\07 Demon Fire.m4a');
    audio.autoplay = true;
    audio.loop = true;
    audio.play();
}

function printd(value, debugMode = True) {
    if (debugMode == true) {
        console.log(value)
    }
}

function loadPage(page) {
    
    const content = document.getElementById('content');
    switch (page) {
      case 'home':
        content.innerHTML = mainPage();
        printd("[Home]", __DEBUG__);
        break;
        
        case 'game':
            content.innerHTML = gamePage();
            printd("[game]", __DEBUG__);
            break;

        case 'battle':
            content.innerHTML = BattlePage();
            printd("[battle]", __DEBUG__);
            break;

      default:
        printd("Fail :(", __DEBUG__);
        content.innerHTML = `<h1>Страница не найдена</h1>`;
    }
  }

function BattlePage() {
    let page = `
                    <style>
                        body { font-family: Arial, sans-serif; text-align: center; }
                        .battle-log { height: 150px; overflow-y: auto; border: 1px solid #000; padding: 10px; margin-top: 10px; }
                        button { margin: 5px; padding: 10px; font-size: 16px; }
                    </style>
                    <h1>Бой!</h1>
                    <img src="${player.model}" alt="Игрок" style="width: 100px; height: 100px;">
                    <img src="" alt="Враг" style="width: 100px; height: 100px;">
                    <p id="player-hp">Игрок HP: 100</p>
                    <p id="enemy-hp">Враг HP: 80</p>

                    <button onclick="attack()">Атаковать</button>
                    <button onclick="heal()">Лечиться</button>

                    <div class="battle-log" id="log"></div>`
    return page;
}

function mainPage() {
    let page = `
    <h1>Главная страница</h1>
    `
    return page;
}

function if_in(array, item) {
    return array.includes(item)
}


function generateDungeon(width, height, steps) {
    let save = {}
    let dungeon = Array.from({ length: height }, () => Array(width).fill("0"));
    let x = 0
    let y = 0
    dungeon[y][x] = "1"; // Начальная точка

    for (let i = 0; i < steps; i++) {
        let randDirection = getRandomInt(0, 100);

        if (randDirection < 25 && x + 1 < width) {
            x += 1;  // Движение вправо (более вероятное)
        } else if (randDirection < 50 && x - 1 >= 0) {
            x -= 1;  // Движение влево
        } else if (randDirection < 75 && y + 1 < height) {
            y += 1;  // Движение вниз
        } else if (y - 1 >= 0) {
            y -= 1;  // Движение вверх
        }
        
        dungeon[y][x] = "1";
         
    }

    for (let i = 0; i < (width*height) / 20; i++) {
        let x = getRandomInt(0, width - 1);
        let y = getRandomInt(0, height - 1);
        if (dungeon[y][x] == "1") {dungeon[y][x] = "e";}
    }

    console.log(dungeon)
    save["map"] = dungeon
    save["enemys"] = []
    dungeon[y][x] = "E"
    localStorage.setItem("map", JSON.stringify(dungeon))
    localStorage.setItem("player_pos", JSON.stringify([0, 0]))
    player_pos = [0, 0]

    offset_left = (JSON.parse(localStorage.getItem("player_pos"))[0] - 5) * -1
    offset_top = (JSON.parse(localStorage.getItem("player_pos"))[1] - 5) * -1

    return dungeon;
    
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


function canvasSectorsRender(map, player_pos, left, top, ITEMS) {

    if (map[player_pos[1]][player_pos[0]] == "e") {
        loadPage("battle");
    }

    if (map[player_pos[1]][player_pos[0]] == "E") {

        const content = document.getElementById('content');

        localStorage.setItem("map", "")
        localStorage.setItem("player_pos", "")
        player_pos = [0, 0]

        map = generateDungeon(map_size[0], map_size[1], Math.round((map_size[0]*map_size[1]) / 3));
        localStorage.setItem("map", JSON.stringify(map))
        localStorage.setItem("player_pos", JSON.stringify([0, 0]))

        content.innerHTML = `<button onclick="loadPage('game')">Game</button>`;
        return;
    }

    //if (game == false) {playBGmusic()}
    game = true
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, 32*(map_size[0] + 10), 32*(map_size[1] + 10));

    map = JSON.parse(localStorage.getItem("map"))

    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {

            console.log(map[i][j])
            
            if (map[i][j] != ITEMS["player"]["color"]) {
                ctx.fillStyle = ITEMS[map[i][j]]["color"];
                const img = new Image();
                img.src = ITEMS[map[i][j]]["texture"];
                img.onload = ()=> ctx.drawImage(img, block_size * (j + left), block_size * (i + top), block_size, block_size)

                //ctx.fillStyle = ITEMS[map[i][j]]["color"];
                //ctx.fillRect(block_size * (j + left), block_size * (i + top), block_size, block_size)                    
            }
        }
    }
    ctx.fillStyle = ITEMS["player"]["color"];
    const img = new Image();
    img.src = ITEMS["player"]["texture"];
    //ctx.fillRect(block_size * (player_pos[0] + left), block_size * (player_pos[1] + top), block_size, block_size)
    img.onload = ()=> ctx.drawImage(img, block_size * (player_pos[0] + left), block_size * (player_pos[1] + top), block_size, block_size)

}

function createMatrix(M, N, defaultValue = "0") {
    const matrix = [];
    
    for (let i = 0; i < M; i++) {
        const row = [];
        for (let j = 0; j < N; j++) {
            row.push(defaultValue);  // Можно изменить defaultValue на любое значение
        }
        matrix.push(row);
    }

    return matrix;
}

function move(direction) {



    let map = JSON.parse(localStorage.getItem("map"))
    console.log(player_pos)
    console.log(offset_left, offset_top)
    console.log(map)
    

    if (direction == "up" &&  player_pos[1] > 0 && if_in(stap_blocks, map[player_pos[1]- 1][player_pos[0]])) {
        player_pos[1]--;
        offset_top++;
        //if (player_pos[1] * block_size <= 2 * block_size) {offset_top++}
    }
    if (direction == "down" &&  player_pos[1] < map_size[1] - 1 && if_in(stap_blocks, map[player_pos[1] + 1][player_pos[0]])) {
        player_pos[1]++;
        offset_top--;
        //if (player_pos[1] * block_size >= 2 * block_size) {offset_top--}
        
    }
    if (direction == "right" &&  player_pos[0] < map_size[0] - 1 && if_in(stap_blocks, map[player_pos[1]][player_pos[0] + 1])) {
        player_pos[0]++;
        offset_left--;
        //if (player_pos[0] * block_size >= 2 * block_size) {offset_left--}        
    }
    if (direction == "left" &&  player_pos[0] > 0 && if_in(stap_blocks, map[player_pos[1]][player_pos[0] - 1])) {
        player_pos[0]--;
        offset_left++;
        //if (player_pos[0] * block_size <= 2 * block_size) {offset_left++}
    }
    localStorage.setItem("player_pos", JSON.stringify([0, 0]))
    canvasSectorsRender(JSON.parse(localStorage.getItem("map")), player_pos, offset_left, offset_top, ITEMS);
}


function gamePage() {
    let page = `    <tr>
        <td>
            <div class="ui">

                <!-- Кнопки для управления -->
                <table style="display: inline-block;">
                    <tr>
                      <th></th>
                      <th><button id="up" class="button" onclick="move('up')">↑</button></th>
                      <th></th>
                    </tr>
                    <tr>
                      <td><button id="left" class="button" onclick="move('left')">←</button></td>
                      <td></td>
                      <td><button id="right" class="button" onclick="move('right')">→</button></td>
                    </tr>
                    <tr>
                      <td></td>
                      <td><button id="down" class="button" onclick="move('down')">↓</button></td>
                      <td></td>
                    </tr>
                  </table>

            </div>
        </td>

        <td>
            
        </td>
    </tr>

    <canvas id="canvas" width="900px" height="380px" onclick="canvasSectorsRender(map, player_pos, offset_left, offset_top)"></canvas>
`
return page;
}


`Блок боя!!!`

// Объекты игрока и врага
let player = { hp: 100, attack: 15, healAmount: 10, model: ITEMS["player"]["model"] };
let enemy = { hp: 80, attack: 10 };

// Функция атаки
function attack() {
    enemy.hp -= player.attack;
    logMessage(`Игрок атакует! Враг теряет ${player.attack} HP.`);
    updateHP();

    if (enemy.hp <= 0) return endGame("Игрок победил!");

    enemyTurn();
}

// Функция лечения
function heal() {
    player.hp += player.healAmount;
    logMessage(`Игрок лечится и восстанавливает ${player.healAmount} HP.`);
    updateHP();

    enemyTurn();
}

// Ход врага
function enemyTurn() {
    let damage = enemy.attack;
    player.hp -= damage;
    logMessage(`Враг атакует! Игрок теряет ${damage} HP.`);
    updateHP();

    if (player.hp <= 0) endGame("Враг победил!");
}

// Обновление интерфейса
function updateHP() {
    document.getElementById("player-hp").innerText = `Игрок HP: ${player.hp}`;
    document.getElementById("enemy-hp").innerText = `Враг HP: ${enemy.hp}`;
}

// Лог боя
function logMessage(message) {
    let log = document.getElementById("log");
    log.innerHTML += `<p>${message}</p>`;
    log.scrollTop = log.scrollHeight; // Прокрутка вниз
}

// Завершение игры
function endGame(message) {
    logMessage(`<strong>${message}</strong>`);
    document.querySelectorAll("button").forEach(btn => btn.disabled = true);
    map_new = JSON.parse(localStorage.getItem("map"))
    map_new[player_pos[1]][player_pos[0]] = "1"
    localStorage.setItem("map", JSON.stringify(map_new))
    loadPage("game");

}