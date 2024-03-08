function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Function to send a POST request with CSRF token
function sendPostRequest() {
}

fetch('/api/tasks/').then(response => response.json()).then(data => {
    const taskList = document.getElementById("taskList");
    console.log(data)
    data.forEach((value) => {
        const li = document.createElement("li");
        const btn = document.createElement("button");
        const complete = document.createElement("button");
        btn.textContent = "Delete";
        complete.textContent = "Complete";
        const csrfToken = getCookie('csrftoken');
        complete.onclick = () => {
            fetch(`/api/task/${value.id}/`, {
                method: 'PATCH',
                body: JSON.stringify({"status": "completed"}),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // Include the CSRF token in the header
                },
            }).then(response => response.json()).then(data => {
                window.location.href = "/"
            })
        };
        btn.onclick = () => {
            fetch(`/api/task/${value.id}/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // Include the CSRF token in the header
                },
            }).then(response => response.json()).then(data => {
                window.location.href = "/"
            })
            li.remove();
        };
        // btn.href = `/api/task/delete/${value.id}/`;
        li.textContent = value.title;
        if (value.status == "completed"){
            li.style.textDecoration = "line-through";
        }
        taskList.appendChild(li);
        li.appendChild(btn);
        li.appendChild(complete)
    });
});
