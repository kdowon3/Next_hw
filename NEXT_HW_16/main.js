document.addEventListener("DOMContentLoaded", () => {
    const content = document.getElementById("content");
    const contentHeading = content.querySelector("h1");
    const navButtons = document.querySelectorAll(".nav-button");

    const colors = {
        about: "red",
        products: "blue",
        technology: "green",
        downloads: "#FFD700" // 눈이 덜 아픈 노란색 계열 (골드)
    };


    navButtons.forEach(button => {
        button.addEventListener("mouseover", () => {
            if (!button.classList.contains("active")) {
                button.style.backgroundColor = colors[button.id];
            }
        });

        button.addEventListener("mouseout", () => {
            if (!button.classList.contains("active")) {
                button.style.backgroundColor = "#666"; // 원래 배경색으로 변경
            }
        });

        button.addEventListener("click", () => {
            navButtons.forEach(btn => {
                btn.classList.remove("active");
                btn.style.backgroundColor = "#666"; // 원래 배경색으로 변경
            });

            button.classList.add("active");

            contentHeading.textContent = button.id.charAt(0).toUpperCase() + button.id.slice(1);
            content.style.backgroundColor = colors[button.id];
            button.style.backgroundColor = colors[button.id]; // 버튼 배경색도 동일하게 설정
        });
    });
});
