var board = {'a8': {'team': 'black', 'type': 'rook', 'moved': false}, 'b8': {'team': 'black', 'type': 'knight', 'moved': false}, 'c8': {'team': 'black', 'type': 'bishop', 'moved': false}, 'd8': {'team': 'black', 'type': 'queen', 'moved': false}, 'e8': {'team': 'black', 'type': 'king', 'moved': false}, 'f8': {'team': 'black', 'type': 'bishop', 'moved': false}, 'g8': {'team': 'black', 'type': 'knight', 'moved': false}, 'h8': {'team': 'black', 'type': 'rook', 'moved': false}, 'a7': {'team': 'black', 'type': 'pawn', 'moved': false}, 'b7': {'team': 'black', 'type': 'pawn', 'moved': false}, 'c7': {'team': 'black', 'type': 'pawn', 'moved': false}, 'd7': {'team': 'black', 'type': 'pawn', 'moved': false}, 'e7': {'team': 'black', 'type': 'pawn', 'moved': false}, 'f7': {'team': 'black', 'type': 'pawn', 'moved': false}, 'g7': {'team': 'black', 'type': 'pawn', 'moved': false}, 'h7': {'team': 'black', 'type': 'pawn', 'moved': false}, 'a2': {'team': 'white', 'type': 'pawn', 'moved': false}, 'b2': {'team': 'white', 'type': 'pawn', 'moved': false}, 'c2': {'team': 'white', 'type': 'pawn', 'moved': false}, 'd2': {'team': 'white', 'type': 'pawn', 'moved': false}, 'e2': {'team': 'white', 'type': 'pawn', 'moved': false}, 'f2': {'team': 'white', 'type': 'pawn', 'moved': false}, 'g2': {'team': 'white', 'type': 'pawn', 'moved': false}, 'h2': {'team': 'white', 'type': 'pawn', 'moved': false}, 'a1': {'team': 'white', 'type': 'rook', 'moved': false}, 'b1': {'team': 'white', 'type': 'knight', 'moved': false}, 'c1': {'team': 'white', 'type': 'bishop', 'moved': false}, 'd1': {'team': 'white', 'type': 'queen', 'moved': false}, 'e1': {'team': 'white', 'type': 'king', 'moved': false}, 'f1': {'team': 'white', 'type': 'bishop', 'moved': false}, 'g1': {'team': 'white', 'type': 'knight', 'moved': false}, 'h1': {'team': 'white', 'type': 'rook', 'moved': false}}
var itsAITurn = false
var selected_piece = '';
var pieces = {
    'black': {
        'rook': '&#9820',
        'knight': '&#9822',
        'bishop': '&#9821',
        'queen': '&#9819',
        'king': '&#9818',
        'pawn': '&#9823'
    },
    'white': {
        'rook': '&#9814',
        'knight': '&#9816',
        'bishop': '&#9815',
        'queen': '&#9813',
        'king': '&#9812',
        'pawn': '&#9817'
    }
}
var legal_sequence = [];
var isPawnPromotion = false;
var clickedBoardHouseIdPawnPromotion = '';

async function sleep(milliseconds) {
    return  await new Promise(resolve => setTimeout(resolve, milliseconds));
}

function redirectToFinalPage(winner) {
    if (winner === 'drawn' || winner === 'ia') {
        window.location.href = window.location.origin+"/defeat/";
    } else if(winner === 'player') {
        window.location.href = window.location.origin+"/victory/";
    }
}

function functionIsGameOver(str) {
    $.ajax({
        url: '/get_is_game_over/',
        type: 'GET',
        success: function(response) {
            isGameOver =  response['is_game_over'];
            if (isGameOver) {
                console.log(isGameOver)
                redirectToFinalPage(response['winner']);
            }
        }
    });
}

function initialBoard(){
    document.getElementById('a8').innerHTML = '&#9820;';
    document.getElementById('b8').innerHTML = '&#9822;';
    document.getElementById('c8').innerHTML = '&#9821;';
    document.getElementById('d8').innerHTML = '&#9819;';
    document.getElementById('e8').innerHTML = '&#9818;';
    document.getElementById('f8').innerHTML = '&#9821;';
    document.getElementById('g8').innerHTML = '&#9822;';
    document.getElementById('h8').innerHTML = '&#9820;';
        
    document.getElementById('a7').innerHTML = '&#9823;';
    document.getElementById('b7').innerHTML = '&#9823;';
    document.getElementById('c7').innerHTML = '&#9823;';
    document.getElementById('d7').innerHTML = '&#9823;';
    document.getElementById('e7').innerHTML = '&#9823;';
    document.getElementById('f7').innerHTML = '&#9823;';
    document.getElementById('g7').innerHTML = '&#9823;';
    document.getElementById('h7').innerHTML = '&#9823;';
        
    document.getElementById('a1').innerHTML = '&#9814;';
    document.getElementById('b1').innerHTML = '&#9816;';
    document.getElementById('c1').innerHTML = '&#9815;';
    document.getElementById('d1').innerHTML = '&#9813;';
    document.getElementById('e1').innerHTML = '&#9812;';
    document.getElementById('f1').innerHTML = '&#9815;';
    document.getElementById('g1').innerHTML = '&#9816;';
    document.getElementById('h1').innerHTML = '&#9814;';
        
    document.getElementById('a2').innerHTML = '&#9817;';
    document.getElementById('b2').innerHTML = '&#9817;';
    document.getElementById('c2').innerHTML = '&#9817;';
    document.getElementById('d2').innerHTML = '&#9817;';
    document.getElementById('e2').innerHTML = '&#9817;';
    document.getElementById('f2').innerHTML = '&#9817;';
    document.getElementById('g2').innerHTML = '&#9817;';
    document.getElementById('h2').innerHTML = '&#9817;';
}

function cleanBoard(){
    // 'limpa' tabuleiro após seleção de alguma casa
    // pinta tabuleiro com cores iniciais

    const black = ['a2', 'a4', 'a6', 'a8', 'b1', 'b3', 'b5', 'b7', 'c2', 'c4', 'c6', 'c8', 'd1', 'd3', 'd5', 'd7', 'e2', 'e4', 'e6', 'e8', 'f1', 'f3', 'f5', 'f7', 'g2', 'g4', 'g6', 'g8', 'h1', 'h3', 'h5', 'h7']
    const white = ['a1', 'a3', 'a5', 'a7', 'b2', 'b4', 'b6', 'b8', 'c1', 'c3', 'c5', 'c7', 'd2', 'd4', 'd6', 'd8', 'e1', 'e3', 'e5', 'e7', 'f2', 'f4', 'f6', 'f8', 'g1', 'g3', 'g5', 'g7', 'h2', 'h4', 'h6', 'h8']

    for(let i = 0; i < black.length; i++) {
        const boardHouse = document.getElementById(black[i]);
        boardHouse.style.backgroundColor = '#777676';
    }

    for(let i = 0; i < white.length; i++) {
        const boardHouse = document.getElementById(white[i]);
        boardHouse.style.backgroundColor = '#e2dddd';
    }
}

function getLegalMoviments(boardHouse) {
    const data = {'id': boardHouse};
    $.ajax({
        url: '/get_moviments/',
        type: 'GET',
        data: data,
        success: function(response) {
            const legal_moves =  response['legal_moves'];
            //console.log('legal moves, id ', boardHouse, ' = ',legal_moves);
            legal_sequence = legal_moves;
            for(let i = 0; i < legal_moves.length; i++) {
                hightlight(legal_moves[i]);
            }
        }
    });
}

function movePiece(oldPiece, newPiece, type_of_piece) {
    const data = {'old_piece': oldPiece, 'new_piece': newPiece, 'type_of_piece': type_of_piece};
    $.ajax({
        url: '/move_piece/',
        type: 'GET',
        data: data,
        success: function(response) {
            new_board =  response['new_board'];
            board = new_board;
            drawBoard(new_board);
            functionIsGameOver('');
        }
    });
}

function drawBoard(new_board) {
    const boardKeys = Object.keys(new_board)
    const boardKeysFull = ['a2', 'a4', 'a6', 'a8', 'b1', 'b3', 'b5', 'b7', 'c2', 'c4', 'c6', 'c8', 'd1', 'd3', 'd5', 'd7', 'e2', 'e4', 'e6', 'e8', 'f1', 'f3', 'f5', 'f7', 'g2', 'g4', 'g6', 'g8', 'h1', 'h3', 'h5', 'h7',
    'a1', 'a3', 'a5', 'a7', 'b2', 'b4', 'b6', 'b8', 'c1', 'c3', 'c5', 'c7', 'd2', 'd4', 'd6', 'd8', 'e1', 'e3', 'e5', 'e7', 'f2', 'f4', 'f6', 'f8', 'g1', 'g3', 'g5', 'g7', 'h2', 'h4', 'h6', 'h8']

    for (let i = 0; i < boardKeysFull.length; i++) {
        const id = boardKeysFull[i];
        if(boardKeys.includes(id)) {
            const piece = pieces[new_board[id].team][new_board[id].type] + ';';
            document.getElementById(id).innerHTML = piece;  
        } else {
            document.getElementById(id).innerHTML = '';
        }
    }
}

function hightlight(idBoardHouse) {
    const boardHouse = document.getElementById(idBoardHouse);
    boardHouse.style.backgroundColor = '#9370DB';
}

function getIAMove() {
    if(itsAITurn) {
        return $.ajax({
            url: '/get_ai_move/',
            type: 'GET',
            success: function(response) {
                new_board =  response['new_board'];
                board = new_board;
                drawBoard(new_board);
                itsAITurn = false;
                functionIsGameOver('');
            }
        });
    }
}


function activePawnPromotion() {
    const ids = ['rook', 'knight', 'bishop', 'queen'];
    for (let index = 0; index < ids.length; index++) {
        const id = ids[index];
        const boardHouse = document.getElementById(id);
        boardHouse.style.backgroundColor = '#9370db';
    }
}

function disablePawnPromotion() {
    const ids = ['rook', 'knight', 'bishop', 'queen'];
    for (let index = 0; index < ids.length; index++) {
        const id = ids[index];
        const boardHouse = document.getElementById(id);
        boardHouse.style.backgroundColor = '#e2dddd';
    }
}

$('.board2').on('click', '.pawn-promotion', async function() {
    if(isPawnPromotion && clickedBoardHouseIdPawnPromotion !== '') {
        const typeOfPiece = $(this).attr('id');

        movePiece(selected_piece, clickedBoardHouseIdPawnPromotion, typeOfPiece);
        
        selected_piece = '';
        itsAITurn = true;
        isPawnPromotion = false;
        disablePawnPromotion();
        clickedBoardHouseIdPawnPromotion = '';
        
        await sleep(300);
        console.log('Board antes da IA => ', board);
        getIAMove();
        console.log('Board depois da IA => ', board);
    }
});

$('.board').on('click', '.board-house', async function() {
    if (!itsAITurn) {
        cleanBoard();
        const clickedBoardHouseId = $(this).attr('id');
        const boardHouse = document.getElementById(clickedBoardHouseId)
        
        if (!isPawnPromotion) {
            // se tem peça na casa selecionada e ela é branca
            if(boardHouse.innerText !== '' && board[clickedBoardHouseId].team === 'white') {
                selected_piece = clickedBoardHouseId;
                hightlight(clickedBoardHouseId);
                getLegalMoviments(clickedBoardHouseId);
            } else if (board[selected_piece].type === 'pawn' && clickedBoardHouseId.includes('8')) {
                if (legal_sequence.includes(clickedBoardHouseId)) {
                    clickedBoardHouseIdPawnPromotion = clickedBoardHouseId;
                    isPawnPromotion = true;
                    activePawnPromotion();
                }
            } else if(boardHouse.innerText === '' && selected_piece !== ''){ // se a casa selecionada está vazia e tem peça selecionada
                movePiece(selected_piece, clickedBoardHouseId, '');
                if (legal_sequence.includes(clickedBoardHouseId)) {
                    selected_piece = '';
                    itsAITurn = true;
                }
                await sleep(300);
                console.log('Board antes da IA => ', board);
                let iaMove = getIAMove();
                await iaMove.done(() => {
                    console.log('Board depois da IA => ', board);
                })
                console.log('Board depois da IA => ', board);
            } else if (boardHouse.innerText !== '' && board[clickedBoardHouseId].team === 'black' && selected_piece !== '') {
                movePiece(selected_piece, clickedBoardHouseId, '');
                if (legal_sequence.includes(clickedBoardHouseId)) {
                    selected_piece = '';
                    itsAITurn = true;
                }
                await sleep(300);
                console.log('Board antes da IA => ', board);
                getIAMove();
                console.log('Board depois da IA => ', board);
            }
        }   
    }
});
