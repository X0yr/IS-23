

function show(){
    alert('Внимательно вводите своё имя');
}
function handle(){
    let name1 = document.getElementById("name").value;
    let chek1 = document.getElementById("cd1").checked;
    let chek2 = document.getElementById("cd2").checked;
    if (chek1 && !chek2){
        alert('Вы выбрали мороженное');
    }
    else if(!chek1 && chek2){
        alert('Вы выбрали шоколад');
    }
    else if(chek1 && chek2){
        alert('Вы выбрали: мороженное и шоколад');
    }
    else{
        alert('Вы ничего не выбрали')
    }
    alert('Спасибо что приняли участие '+ name1)
}
