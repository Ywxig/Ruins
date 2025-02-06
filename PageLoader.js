
__DEBUG__ = true
player_pos = [0, 0]
block_size = 32
canvas_size = [3,3]
map_size = [10,10]
map = createMatrix(map_size[0], map_size[1], defaultValue = '0');


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

      default:
        printd("Fail :(", __DEBUG__);
        content.innerHTML = `<h1>Страница не найдена</h1>`;
    }
  }

function mainPage() {
    let page = `
    <h1>Главная страница</h1>
    `
    return page;
}

function consoleMapRender(map, player_pos) {
    map[player_pos[1]][player_pos[0]] = "@";
    let arr = [];
    for (let x = 0; x < map.length; x++) {
        arr.push(map[x].join(""))
    }
    console.log(arr.join("\n"))
    map[player_pos[1]][player_pos[0]] = "0";
}

function canvasMapRender(map, player_pos) {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {
            if (map[i][j] == "0") { // если блок это пустое место то отрисовывается соответствующая текстура
                ctx.fillStyle = "green";
                ctx.fillRect(block_size * i, block_size * j, block_size, block_size)                
            }
            
        }
        ctx.fillStyle = "violet";
        ctx.fillRect(block_size * player_pos[0], block_size * player_pos[1], block_size, block_size)   
    }
}

function canvasSectorsRender(map, player_pos, left, top) {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {
            if (map[i][j] == "0") { // если блок это пустое место то отрисовывается соответствующая текстура
                ctx.fillStyle = "green";
                ctx.fillRect(block_size * (i + left), block_size * (j + top), block_size, block_size)                
            }

            if (map[i][j] == "1") { // если блок это пустое место то отрисовывается соответствующая текстура
                ctx.fillStyle = "blue";
                ctx.fillRect(block_size * (i + left), block_size * (j + top), block_size, block_size)                
            }
        }
        ctx.fillStyle = "violet";
        ctx.fillRect(block_size * (player_pos[0] + left), block_size * (player_pos[1] + top), block_size, block_size)   
    }
}

function createMatrix(M, N, defaultValue = 0) {
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
    
    if (direction == "up") {
        player_pos[1]--;
        //if(player_pos[1] * block_size[1] > 2 * block_size[1]){top = top - block_size[1]}
    }
    if (direction == "down") {
        player_pos[1]++;
        //if(player_pos[1] * block_size[1] < canvas_size[1] * block_size[1]){top = top + block_size[1]}
    }
    if (direction == "right") {
        player_pos[0]++;
        //if(player_pos[0] * block_size[0] > canvas_size[0] * block_size[0]){left = left - block_size[0]}
    }
    if (direction == "left") {
        player_pos[0]--;
        left = left + block_size[0]
        //if(player_pos[0] * block_size[0] > 2 * block_size[0]){top = top - block_size[0]}
    }
    canvasSectorsRender(map, player_pos, left, top);
}


function gamePage() {
    const content = document.getElementById('content');
    while (game = true) {
        printd("[game stap]", __DEBUG__);
        printd("", __DEBUG__);
        content.innerHTML = mainPage();
    }
}

function canvasMove(direction) {
    const canvas = document.getElementById("canvas");

    // Получаем текущие значения left и top
    let currentLeft = canvas.style.left;  // если не задано, то по умолчанию 0
    let currentTop =  canvas.style.top;

    // Размер сдвига (например, на 20 пикселей)
    const moveAmount = 20;

    // Отклоняем канвас в зависимости от направления
    if (direction === "left") {
        canvas.style.left = currentLeft - moveAmount + "px";
    } else if (direction === "right") {
        canvas.style.left = currentLeft + moveAmount + "px";
    } else if (direction === "up") {
        canvas.style.top = currentTop - moveAmount + "px";
    } else if (direction === "down") {
        canvas.style.top = currentTop + moveAmount + "px";
    }
}