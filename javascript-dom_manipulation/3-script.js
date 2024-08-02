document.getElementById('toggle_header').addEventListener('click', function(){
    const element = document.querySelector('header');
    if (element.classList.contains('green')){
        element.classList.remove('green');
        element.classList.add('red');
    } else {
        element.classList.add('green');
    }
});
