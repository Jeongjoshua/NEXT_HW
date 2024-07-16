const todoForm = document.getElementById('todo-form');
const todoList = document.getElementById('todo-list');
const contentInput = document.getElementById('content');
const TODO_KEY = 'todoSet';
let todoSet = JSON.parse(localStorage.getItem(TODO_KEY)) || [];

function saveTodos() {
    localStorage.setItem(TODO_KEY, JSON.stringify(todoSet));
}

function deleteTodoFromDOM(todoItem, li) {
    todoSet = todoSet.filter((item) => item !== todoItem);
    saveTodos();
    todoList.removeChild(li);
}

function addTodoToDOM(todo) {
    const li = document.createElement('li');
    li.textContent = todo;

    const deleteButton = document.createElement('button');
    deleteButton.textContent = '삭제';
    deleteButton.onclick = () => {
        deleteTodoFromDOM(todo, li);
    };

    li.appendChild(deleteButton);
    todoList.appendChild(li);
}

function addTodo(event) {
    event.preventDefault();
    const newTodo = contentInput.value.trim();
    if (newTodo) {
        todoSet.push(newTodo);
        saveTodos();
        addTodoToDOM(newTodo);
        contentInput.value = '';
    }
}

function clearTodoList() {
    // Clear the to-do list from local storage
    localStorage.removeItem(TODO_KEY);

    // Clear the in-memory to-do list
    todoSet = [];

    // Remove all items from the to-do list in the DOM
    while (todoList.firstChild) {
        todoList.removeChild(todoList.firstChild);
    }
}

todoForm.addEventListener('submit', addTodo);

// Load todos from local storage when the page is loaded
window.addEventListener('DOMContentLoaded', () => {
    todoSet.forEach(addTodoToDOM);
});

// Ensure the to-do list is cleared when the username is reset
window.resetUsername = (function (originalFunction) {
    return function () {
        clearTodoList();
        originalFunction();
    };
})(window.resetUsername);
