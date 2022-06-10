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

function callEasyGame(){
    console.log('Implementação em andamento...')
}

function callHardGame(){
    console.log('Implementação em andamento...')
}

function callPlay() {
    alert('play!!!')
    $.ajax({
        url: '/levels/',
        type: 'GET',
        success: function (response) {
            console.log(response);
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
        // cache: false,
        // processData: false,
        // contentType: false,
        success: function(response) {
            const legal_moves =  response['legal_moves'];
            console.log(legal_moves);
            for(let i = 0; i < legal_moves.length; i++) {
                hightlight(legal_moves[i]);
            }
        }
    });
}

function movePiece(oldPiece, newPiece) {
    const data = {'old_piece': oldPiece, 'new_piece': newPiece};
    $.ajax({
        url: '/move_piece/',
        type: 'GET',
        data: data,
        success: function(response) {
            board =  response['new_board'];
        }
    });
}

function drawBoard() {
    console.log('entrou')
    const boardKeys = Object.keys(board)
    const boardKeysFull = ['a2', 'a4', 'a6', 'a8', 'b1', 'b3', 'b5', 'b7', 'c2', 'c4', 'c6', 'c8', 'd1', 'd3', 'd5', 'd7', 'e2', 'e4', 'e6', 'e8', 'f1', 'f3', 'f5', 'f7', 'g2', 'g4', 'g6', 'g8', 'h1', 'h3', 'h5', 'h7',
    'a1', 'a3', 'a5', 'a7', 'b2', 'b4', 'b6', 'b8', 'c1', 'c3', 'c5', 'c7', 'd2', 'd4', 'd6', 'd8', 'e1', 'e3', 'e5', 'e7', 'f2', 'f4', 'f6', 'f8', 'g1', 'g3', 'g5', 'g7', 'h2', 'h4', 'h6', 'h8']
    console.log('chegou', boardKeysFull.length)
    
    for (let i = 0; i < boardKeysFull.length; i++) {
        const id = boardKeysFull[i];
        //console.log('id -> ', id)
        if(boardKeys.includes(id)) {
            const piece = pieces[board[id].team][board[id].type] + ';';
            console.log(piece, id)
            console.log(document.getElementById(id).innerHTML)
            document.getElementById(id).innerHTML = piece;
            console.log(document.getElementById(id).innerHTML)
        } else {
            document.getElementById(id).innerHTML = '';
        }
    }

    // for (let i = 0; i < boardKeysFull.lenght; i++) {
    //     console.log('i = ', i)
    //     console.log('aaa = ', boardKeysFull[i])
    //     const id = boardKeysFull[i];
    //     if(boardKeys.includes(id)) {
    //         console.log('abc = ', id)
    //         document.getElementById(id).innerHTML = pieces[board[id].team][board[id].type];
    //     } else {
    //         console.log('def = ', id)
    //         document.getElementById(id).innerHTML = '';
    //     }
    // }
}

function hightlight(idBoardHouse) {
    const boardHouse = document.getElementById(idBoardHouse);
    boardHouse.style.backgroundColor = '#9370DB';
}

$('.board').on('click', '.board-house', function() {
    if (!itsAITurn) {
        cleanBoard();
        const clickedBoardHouseId = $(this).attr('id');
        const boardHouse = document.getElementById(clickedBoardHouseId)
        
        if(boardHouse.innerText !== '' && board[clickedBoardHouseId].team === 'white') {
            selected_piece = clickedBoardHouseId;
            hightlight(clickedBoardHouseId);
            getLegalMoviments(clickedBoardHouseId);
        } else if(boardHouse.innerText === '' && selected_piece !== ''){
            // const piece = pieces[board[selected_piece].team][board[selected_piece].type]
            // boardHouse.innerHTML = piece + ';';
            // document.getElementById(selected_piece).innerHTML = '';
            movePiece(selected_piece, clickedBoardHouseId)
            drawBoard()
            selected_piece = ''
            itsAITurn = true
        }
    }
});

function ia_movement() {
    if(itsAITurn) {
        // get mov da IA
    }
    itsAITurn = false
}

//////////////////////////////////////////////////////////

// function initialLoad(){
    
//     //Primeiro movimento começa com as peças brancas
//     turn = 'white'; 
    
//     //Colocar as peças no tabuleiro
//     document.getElementById('a8').innerHTML = '&#9820;';
//     document.getElementById('b8').innerHTML = '&#9822;';
//     document.getElementById('c8').innerHTML = '&#9821;';
//     document.getElementById('d8').innerHTML = '&#9819;';
//     document.getElementById('e8').innerHTML = '&#9818;';
//     document.getElementById('f8').innerHTML = '&#9821;';
//     document.getElementById('g8').innerHTML = '&#9822;';
//     document.getElementById('h8').innerHTML = '&#9820;';
        
//     document.getElementById('a7').innerHTML = '&#9823;';
//     document.getElementById('b7').innerHTML = '&#9823;';
//     document.getElementById('c7').innerHTML = '&#9823;';
//     document.getElementById('d7').innerHTML = '&#9823;';
//     document.getElementById('e7').innerHTML = '&#9823;';
//     document.getElementById('f7').innerHTML = '&#9823;';
//     document.getElementById('g7').innerHTML = '&#9823;';
//     document.getElementById('h7').innerHTML = '&#9823;';
        
//     document.getElementById('a1').innerHTML = '&#9814;';
//     document.getElementById('b1').innerHTML = '&#9816;';
//     document.getElementById('c1').innerHTML = '&#9815;';
//     document.getElementById('d1').innerHTML = '&#9813;';
//     document.getElementById('e1').innerHTML = '&#9812;';
//     document.getElementById('f1').innerHTML = '&#9815;';
//     document.getElementById('g1').innerHTML = '&#9816;';
//     document.getElementById('h1').innerHTML = '&#9814;';
        
//     document.getElementById('a2').innerHTML = '&#9817;';
//     document.getElementById('b2').innerHTML = '&#9817;';
//     document.getElementById('c2').innerHTML = '&#9817;';
//     document.getElementById('d2').innerHTML = '&#9817;';
//     document.getElementById('e2').innerHTML = '&#9817;';
//     document.getElementById('f2').innerHTML = '&#9817;';
//     document.getElementById('g2').innerHTML = '&#9817;';
//     document.getElementById('h2').innerHTML = '&#9817;';	
        
    
//     var x, y;
    
//     //Array para receber as posições do tabuleiro
//     piece = new Array();
            
//     for(x=1;x<=8;x++){
                
//         piece[x] = new Array();
                
//         for(y=1;y<=8;y++){
                
//             piece[x][y] = new Array();
//             piece[x][y]['piece'] = false; 		
//             piece[x][y]['color'] = false;			
                 
//         }
//     }    
    
//     aux = new Array();
//     aux['black'] = new Array();
//     aux['white'] = new Array();    
           
//     //Coloca as peças pretas no array de posições
//     piece[1][1]['piece']='rook';		piece[1][1]['color']='black';	piece[1][1]['mov']=0; aux['black']['rook'] = '&#9820;';
//     piece[1][2]['piece']='knight';  	piece[1][2]['color']='black';	piece[1][2]['mov']=0; aux['black']['knight'] = '&#9822;';
//     piece[1][3]['piece']='bishop'; 	    piece[1][3]['color']='black';	piece[1][3]['mov']=0; aux['black']['bishop'] = '&#9821;';
//     piece[1][4]['piece']='queen';	    piece[1][4]['color']='black';	piece[1][4]['mov']=0; aux['black']['queen'] = '&#9819;';
//     piece[1][5]['piece']='king';		piece[1][5]['color']='black';	piece[1][5]['mov']=0; aux['black']['king'] = '&#9818;';
//     piece[1][6]['piece']='bishop';		piece[1][6]['color']='black';	piece[1][6]['mov']=0; 
//     piece[1][7]['piece']='knight';   	piece[1][7]['color']='black';	piece[1][7]['mov']=0; 
//     piece[1][8]['piece']='rook';		piece[1][8]['color']='black';	piece[1][8]['mov']=0; 
    
//     piece[2][1]['piece']='pawn';		piece[2][1]['color']='black';	piece[2][1]['mov']=0; aux['black']['pawn'] = '&#9823;';
//     piece[2][2]['piece']='pawn';		piece[2][2]['color']='black';	piece[2][2]['mov']=0;
//     piece[2][3]['piece']='pawn'; 		piece[2][3]['color']='black';	piece[2][3]['mov']=0;
//     piece[2][4]['piece']='pawn';		piece[2][4]['color']='black';	piece[2][4]['mov']=0;
//     piece[2][5]['piece']='pawn';		piece[2][5]['color']='black';	piece[2][5]['mov']=0;
//     piece[2][6]['piece']='pawn';		piece[2][6]['color']='black';	piece[2][6]['mov']=0;
//     piece[2][7]['piece']='pawn';		piece[2][7]['color']='black';	piece[2][7]['mov']=0;
//     piece[2][8]['piece']='pawn';		piece[2][8]['color']='black';	piece[2][8]['mov']=0;	
    
//     //Coloca as peças brancas no array de posições
//     piece[8][1]['piece']='rook';		piece[8][1]['color']='white';	piece[8][1]['mov']=0; aux['white']['rook'] = '&#9814;';
//     piece[8][2]['piece']='knight';	    piece[8][2]['color']='white';	piece[8][2]['mov']=0; aux['white']['knight'] = '&#9816;';
//     piece[8][3]['piece']='bishop'; 	    piece[8][3]['color']='white';	piece[8][3]['mov']=0; aux['white']['bishop'] = '&#9815;';
//     piece[8][4]['piece']='queen';	    piece[8][4]['color']='white';	piece[8][4]['mov']=0; aux['white']['queen'] = '&#9813;';
//     piece[8][5]['piece']='king';		piece[8][5]['color']='white';	piece[8][5]['mov']=0; aux['white']['king'] = '&#9812;';
//     piece[8][6]['piece']='bishop';		piece[8][6]['color']='white';	piece[8][6]['mov']=0;
//     piece[8][7]['piece']='knight';	    piece[8][7]['color']='white';	piece[8][7]['mov']=0;
//     piece[8][8]['piece']='rook';		piece[8][8]['color']='white';	piece[8][8]['mov']=0;
    
//     piece[7][1]['piece']='pawn';		piece[7][1]['color']='white';	piece[7][1]['mov']=0; aux['white']['pawn'] = '&#9817;';
//     piece[7][2]['piece']='pawn';		piece[7][2]['color']='white';	piece[7][2]['mov']=0;
//     piece[7][3]['piece']='pawn'; 		piece[7][3]['color']='white';	piece[7][3]['mov']=0;
//     piece[7][4]['piece']='pawn';		piece[7][4]['color']='white';	piece[7][4]['mov']=0;
//     piece[7][5]['piece']='pawn';		piece[7][5]['color']='white';	piece[7][5]['mov']=0;
//     piece[7][6]['piece']='pawn';		piece[7][6]['color']='white';	piece[7][6]['mov']=0;
//     piece[7][7]['piece']='pawn';		piece[7][7]['color']='white';	piece[7][7]['mov']=0;
//     piece[7][8]['piece']='pawn';		piece[7][8]['color']='white';	piece[7][8]['mov']=0;	
    
    
    
//     //Array para as movimentações de peças
//     moves = new Array();
        
//     moves['pieceSelected'] = new Array();
//     moves['pieceSelected']['x'] =0;
//     moves['pieceSelected']['y'] =0;
//     moves['pieceSelected']['piece']='0';
//     moves['pieceSelected']['color']='0';
        
//     moves['pieceDestiny'] = new Array();
//     moves['pieceDestiny']['x'] =0;
//     moves['pieceDestiny']['y'] =0; 
//     moves['pieceDestiny']['piece'] ='0';
//     moves['pieceDestiny']['color']='0';
    
//     //Array para os possíveis movimentos
//     possibleMoves = new Array();
    
// }
    
// function possibleMoves_moves(){
//     var x, y;
//     var c = 0; 
//     var i;
//     x = moves['pieceSelected']['x'];
//     y = moves['pieceSelected']['y'];
        
//     //Hightlight nos quadrantes do tabuleiro onde é possível se movimentar
//     document.getElementById('t'+x+y).style.backgroundColor = '#9370DB'; 
//     possibleMoves[c] = 't'+x+y; c++;
    
//     //Movimentos possíveis ao clicar na peça Peão
//     if(piece[x][y]['piece']=='pawn'){

//         if(piece[x][y]['color']=='white'){
//             if(!piece[x-1][y]['piece']){
//                 possible(x-1, y);
//             }if(y-1>0 && piece[x-1][y-1]['piece']){
//                 possible(x-1, y-1);						
//             }
//             if(y+1<9 && piece[x-1][y+1]['piece']){
//                 possible(x-1, y+1);					
//             }					
    
//             if(x==7){				
//                 if(!piece[x-2][y]['piece'] && !piece[x-1][y]['piece']){
//                     possible(x-2, y);
//                 }
//             }
//         }
            
            
//         if(piece[x][y]['color']=='black'){        
//             if(!piece[x+1][y]['piece']){
//                 possible(x+1, y);
//             }if(y-1>0 && piece[x+1][y-1]['piece']){
//                 possible(x+1, y-1);						
//             }
//             if(y+1<9 && piece[x+1][y+1]['piece']){
//                 possible(x+1, y+1);					
//             }					
    
//             if(x==2){
//                 if(!piece[x+2][y]['piece'] && !piece[x+1][y]['piece']){
//                     possible(x+2, y);
//                 }
//             }
    
//         }
//     }
    
//     //Movimentos possíveis ao clicar na peça Cavalo
//     if(piece[x][y]['piece']=='knight'){    
//         possible(x-1, y-2);
//         possible(x+1, y+2);
//         possible(x+1, y-2);
//         possible(x-1, y+2);
//         possible(x-2, y-1);
//         possible(x+2, y+1);
//         possible(x+2, y-1);
//         possible(x-2, y+1);
            
//     }
    
//     //Movimentos possíveis ao clicar na peça Rei
//     if(piece[x][y]['piece']=='king'){
//         possible(x-1, y);
//         possible(x, y-1);
//         possible(x-1, y-1);
//         possible(x+1, y);
//         possible(x, y+1);
//         possible(x+1, y+1);
//         possible(x-1, y+1);
//         possible(x+1, y-1);
//     }
    
//     //Movimentos possíveis ao clicar na peça Torre
//     if(piece[x][y]['piece']=='rook'){    
//         for(i=1; possible(x-i, y); i++);
//         for(i=1; possible(x+i, y); i++);
//         for(i=1; possible(x, y-i); i++);
//         for(i=1; possible(x, y+i); i++);
//     }
    
//     //Movimentos possíveis ao clicar na peça Bispo

//     if(piece[x][y]['piece']=='bishop'){
//         for(i=1; possible(x-i, y-i);i++);
//         for(i=1; possible(x+i, y+i);i++);
//         for(i=1; possible(x-i, y+i);i++);
//         for(i=1; possible(x+i, y-i);i++);
//     }
    
    
//     //Movimentos possíveis ao clicar na peça Rainha
//     if(piece[x][y]['piece']=='queen'){  
//         for(i=1; possible(x-i, y-i);i++);
//         for(i=1; possible(x+i, y+i);i++);
//         for(i=1; possible(x-i, y+i);i++);
//         for(i=1; possible(x+i, y-i);i++);
//         for(i=1; possible(x-i, y);i++);
//         for(i=1; possible(x+i, y);i++);
//         for(i=1; possible(x, y-i);i++);
//         for(i=1; possible(x, y+i);i++);
        
//     }

//     function possible(px, py){
//         if(px>0 && px <9 && py>0 && py <9 && piece[px][py]['color']!= moves['pieceSelected']['color']){
//             //Hightlight nos quadrantes do tabuleiro onde é possível se movimentar
//             document.getElementById('t'+(px)+(py)).style.backgroundColor = '#9370DB';
//             possibleMoves[c] = 't'+(px)+(py); c++;
                
//             if(!piece[px][py]['piece']){
//                 return true;
//             }
//         }else{
//             return false;
//         }
        
//     }

//     return c;
// }
    
// function noBackground(){
//     var cf;
//     for(cf=0;cf<possibleMoves.length;cf++){
//         document.getElementById(possibleMoves[cf]).style.backgroundColor = '';
//     }	
// }
    
// function check_possible(x, y, c){
//     var chance = 0;
//     var cp;
//     var div = 't'+x+y;
        
//     for(cp=1;cp<c;cp++){
            
//         if(possibleMoves[cp] == div){
//             chance ++;
//         }
//         if(chance > 0){
//             return 1;
//         }
//     }	
// }

// function select(x, y){
//     if((moves['pieceSelected']['x']==0 || piece[x][y]['color'] == moves['pieceSelected']['color']) && piece[x][y]['color']==turn){
//         if(moves['pieceSelected']['x']!=0){
//             noBackground(); 
//         }
//         if(piece[x][y]['piece']){ 
//             moves['pieceSelected']['x'] = x;	
//             moves['pieceSelected']['y'] = y; 
//             moves['pieceSelected']['piece'] = piece[x][y]['piece']; 
//             moves['pieceSelected']['color'] = piece[x][y]['color'];	
                    
//             cont_possibleMoves = possibleMoves_moves();	
//         }        
//     }else if(check_possible(x, y, cont_possibleMoves)){   
//         if(piece[x][y]['piece']=='king'){
//             alert(moves['pieceSelected']['color']+' venceu (:');            
//         }
                
//         if(moves['pieceSelected']['piece']=='pawn' && moves['pieceSelected']['color']=='white' && x==1){
//             document.getElementById('boardBackground').style.display='block';	
//             xe=x;ye=y;
//         }
//         if(moves['pieceSelected']['piece']=='pawn' && moves['pieceSelected']['color']=='black' && x==8){
//             document.getElementById('boardBackground').style.display='block';					
//             xe=x;ye=y;
//         }
                
//         if(piece[x][y]['color'] != moves['pieceSelected']['color']){
//             moves['pieceDestiny']['x']=x;	
//             moves['pieceDestiny']['y']=y;  
 
//             if(piece[x][y]['piece']){  
//                 moves['pieceDestiny']['piece'] = piece[x][y]['piece'];	
//                 moves['pieceDestiny']['color'] = piece[x][y]['color'];	
//             }
                    
//             document.getElementById('t'+moves['pieceSelected']['x']+''+moves['pieceSelected']['y']).innerHTML = ''; 
//             document.getElementById('t'+x+''+y).innerHTML = aux[moves['pieceSelected']['color']][moves['pieceSelected']['piece']]; 
//             piece[x][y]['piece']=moves['pieceSelected']['piece'];	
//             piece[x][y]['color']=moves['pieceSelected']['color'];		
                                    
//             piece[moves['pieceSelected']['x']][moves['pieceSelected']['y']]['piece'] = false;		
//             piece[moves['pieceSelected']['x']][moves['pieceSelected']['y']]['color'] = false;		
                        
//             moves['pieceSelected']['x']=0;	
//             moves['pieceSelected']['y']=0;	
//             moves['pieceSelected']['piece']='0';	
//             moves['pieceSelected']['color']='0';	                               
//         }
    
//         noBackground(); 

//         if(turn=='white'){
//             turn='black';
//         }else{
//             turn='white';
//         } 
//     }
// }