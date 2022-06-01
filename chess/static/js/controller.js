function callMediumGame(){
    console.log('Implementação em andamento...')
}

function callPlay() {
    alert('play!!!')
    $.ajax({
        url: "/levels/",
        type: 'GET',
        success: function (response) {
            console.log(response);
        }
    });
}
