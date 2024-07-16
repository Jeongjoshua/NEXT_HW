function showContent(content) {
    const contentDiv = document.getElementById('content');
    const contentHeader = contentDiv.querySelector('h1');
    const contentParagraph = contentDiv.querySelector('p');
    const buttons = document.querySelectorAll('.nav-button');

    buttons.forEach((button) => button.classList.remove('active'));

    // Change content based on the button clicked
    if (content === 'About') {
        contentHeader.textContent = 'About';
        contentParagraph.textContent = 'Custom Software Development Company';
        contentDiv.className = 'content about';
        buttons[0].classList.add('active');
    } else if (content === 'Products') {
        contentHeader.textContent = 'Products';
        contentParagraph.textContent = 'Our range of software products includes...';
        contentDiv.className = 'content products';
        buttons[1].classList.add('active');
    } else if (content === 'Technology') {
        contentHeader.textContent = 'Technology';
        contentParagraph.textContent = 'We use cutting-edge technology to...';
        contentDiv.className = 'content technology';
        buttons[2].classList.add('active');
    } else if (content === 'Downloads') {
        contentHeader.textContent = 'Downloads';
        contentParagraph.textContent = 'Download our software from the links below...';
        contentDiv.className = 'content downloads';
        buttons[3].classList.add('active');
    }
}
