document.addEventListener("DOMContentLoaded", function() {
    const snowflakesContainer = document.createElement("div");
    snowflakesContainer.className = "snowflakes";
    document.body.appendChild(snowflakesContainer);

    for (let i = 0; i < 50; i++) {
        const snowflake = document.createElement("div");
        snowflake.className = "snowflake";
        snowflake.innerHTML = "❄";
        snowflake.style.color = "#ffffff"; /* Bílá barva vloček */
        snowflake.style.left = `${Math.random() * 100}vw`; /* Náhodná horizontální pozice */
        snowflake.style.animationDuration = `${Math.random() * 3 + 2}s`; /* Náhodná rychlost padání */
        snowflake.style.animationDelay = `${Math.random() * 5}s`; /* Náhodné zpoždění */
        snowflakesContainer.appendChild(snowflake);

        let isDragging = false;
        let offsetX, offsetY;

        snowflake.addEventListener("mousedown", function(event) {
            isDragging = true;
            offsetX = event.clientX - snowflake.getBoundingClientRect().left;
            offsetY = event.clientY - snowflake.getBoundingClientRect().top;
            snowflake.style.cursor = "grabbing"; /* Změna kurzoru při uchopení */
        });

        document.addEventListener("mousemove", function(event) {
            if (isDragging) {
                snowflake.style.left = `${event.clientX - offsetX}px`;
                snowflake.style.top = `${event.clientY - offsetY}px`;
            }
        });

        document.addEventListener("mouseup", function() {
            isDragging = false;
            snowflake.style.cursor = "grab"; /* Změna kurzoru po uvolnění */
        });
    }
});
