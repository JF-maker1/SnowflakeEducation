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
    }
});
