function btnClick(){
    let shape = document.getElementById('shape').value;
    let color = document.getElementById('color').value;
    let length = shape.length;

    let messeg = 'Мне нравиться '+ shape + ', Цвета '+ color + '\n';
    messeg += shape + ' - длинна '+ length;
    alert(messeg);
}