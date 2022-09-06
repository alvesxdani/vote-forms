function headerResize() {
const mainTitle = document.getElementById('main-title');
const fLogo = document.getElementById('logo');


window.addEventListener('resize', () => {
    console.log(window.innerWidth);

    if(window.innerWidth < 570) {
        mainTitle.classList.remove('vh-100');
        mainTitle.classList.add('vh-50','pb-5');
        fLogo.classList.remove('vh-100');
        fLogo.classList.add('vh-50','pb-5','pt-5');
    } else if(window.innerWidth > 570) {
        mainTitle.classList.add('vh-100');
        mainTitle.classList.remove('vh-50');
        fLogo.classList.add('vh-100');
        fLogo.classList.remove('vh-50');
    }
});

window.addEventListener('load', () => {
    console.log(window.innerWidth);

    if(window.innerWidth < 570) {
        mainTitle.classList.remove('vh-100');
        mainTitle.classList.add('vh-50','pb-5');
        fLogo.classList.remove('vh-100');
        fLogo.classList.add('vh-50','pb-5','pt-5');
    } else if(window.innerWidth > 570) {
        mainTitle.classList.add('vh-100');
        mainTitle.classList.remove('vh-50');
        fLogo.classList.add('vh-100');
        fLogo.classList.remove('vh-50');
    }
});
}
headerResize();