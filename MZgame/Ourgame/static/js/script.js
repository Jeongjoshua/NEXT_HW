document.addEventListener('DOMContentLoaded', (event) => {
    const hand = document.getElementById('hand');
    const container = document.getElementById('container');
    const hpBar = document.getElementById('hp-bar');
    const timerElement = document.getElementById('timer');
    let topPosition = 50; // Starting at 50% from the top
    let hp = 100;
    let timeElapsed = 0;
    let objectSpeed = 20; // Initial speed at which objects move towards the hand
    const objectCreationInterval = 2000; // Interval in milliseconds to create objects
    let currentObjectSpeed = objectSpeed;

    // Move the hand up and down
    window.addEventListener('keydown', (e) => {
        switch (e.key) {
            case 'ArrowUp':
                topPosition -= 10;
                if (topPosition < 0) topPosition = 0;
                break;
            case 'ArrowDown':
                topPosition += 10;
                if (topPosition > 100) topPosition = 100;
                break;
        }
        hand.style.top = `${topPosition}%`;
    });

    // Function to create a flying object
    function createObject() {
        const object = document.createElement('img');
        object.src = 'https://cdn.britannica.com/68/195168-050-BBAE019A/football.jpg';
        object.classList.add('object');
        object.style.position = 'absolute'; // Ensure absolute positioning
        object.style.top = `${Math.random() * 100}%`;
        object.style.left = '0%'; // Start at the left edge
        container.appendChild(object);

        // Move the object towards the right
        let objectPosition = 0;
        const interval = setInterval(() => {
            objectPosition += 2; // Increment the position
            object.style.left = `${objectPosition}%`;

            // Check for collision with the hand
            const objectRect = object.getBoundingClientRect();
            const handRect = hand.getBoundingClientRect();
            if (
                objectRect.right >= handRect.left && // Ensure it touches the hand
                objectRect.left <= handRect.right && // Ensure it overlaps horizontally
                objectRect.top < handRect.bottom && // Ensure it overlaps vertically
                objectRect.bottom > handRect.top // Ensure it overlaps vertically
            ) {
                clearInterval(interval);
                container.removeChild(object);
            } else if (objectRect.left >= window.innerWidth) {
                // Check if the object is off the right edge
                // If the object reaches the right end
                clearInterval(interval);
                container.removeChild(object);
                hp -= 10;
                hpBar.style.width = `${hp}%`;
                if (hp <= 0) {
                    alert('Game Over!');
                    clearInterval(timerInterval);
                    location.reload();
                }
            }
        }, currentObjectSpeed);
    }

    // Create objects at intervals
    const objectInterval = setInterval(createObject, objectCreationInterval);

    // Timer to update elapsed time and increase speed
    const timerInterval = setInterval(() => {
        timeElapsed += 1;
        timerElement.textContent = `Time: ${timeElapsed}s`;

        // Increase speed every 10 seconds
        if (timeElapsed % 10 === 0) {
            currentObjectSpeed = Math.max(5, currentObjectSpeed * 0.5); // Increase speed by 50%
        }
    }, 1000);
});
