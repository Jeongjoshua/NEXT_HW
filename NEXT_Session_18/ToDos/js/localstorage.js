const username = document.querySelector('.username');
const usernameWrapper = document.querySelector('.usernameWrapper');
const header = document.querySelector('#header');

function setUsername() {
    window.localStorage.setItem('username', username.value);
    checkUsername();
}
function checkUsername() {
    const checkName = window.localStorage.getItem('username');
    usernameWrapper.style.display = 'none';
    if (checkName) {
        header.innerHTML = `<h1>${checkName}의 ToDoList</h1><button type = "button" onclick="resetUsername()">초기화</button>`;
    } else {
        header.innerHTML = ``;
        usernameWrapper.style.display = 'flex';
    }
}

function resetUsername() {
    window.localStorage.removeItem('username');
    checkUsername();
}
