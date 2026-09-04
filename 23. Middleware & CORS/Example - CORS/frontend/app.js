const API_URL = "http://127.0.0.1:8000";
const addForm = document.querySelector("#add-form");
const idForm = document.querySelector("#id-form");
const deleteButton = document.querySelector("#delete-button");
const showAllButton = document.querySelector("#show-all-button");
const studentsList = document.querySelector("#students-list");
const result = document.querySelector("#result");

function showMessage(message, type = "success", student = null) {
  result.hidden = false;
  result.className = `result ${type}`;
  result.replaceChildren();

  const heading = document.createElement("strong");
  heading.textContent = message;
  result.append(heading);

  if (student) {
    const details = document.createElement("p");
    details.textContent = `ID: ${student.id} · Name: ${student.name} · Age: ${student.age}`;
    result.append(details);
  }
}

async function errorMessage(response) {
  try {
    const body = await response.json();
    if (Array.isArray(body.detail)) {
      return body.detail.map((item) => item.msg).join(", ");
    }
    return body.detail || "The request failed";
  } catch {
    return "The request failed";
  }
}

addForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const payload = {
    name: document.querySelector("#name").value,
    age: Number(document.querySelector("#age").value),
  };

  try {
    const response = await fetch(`${API_URL}/students`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (!response.ok) throw new Error(await errorMessage(response));

    const student = await response.json();
    showMessage("Student added successfully.", "success", student);
    document.querySelector("#student-id").value = student.id;
    addForm.reset();
  } catch (error) {
    showMessage(error.message || "Could not reach the API.", "error");
  }
});

idForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const id = document.querySelector("#student-id").value;

  try {
    const response = await fetch(`${API_URL}/students/${id}`);
    if (!response.ok) throw new Error(await errorMessage(response));
    showMessage("Student found.", "success", await response.json());
  } catch (error) {
    showMessage(error.message || "Could not reach the API.", "error");
  }
});

deleteButton.addEventListener("click", async () => {
  if (!idForm.reportValidity()) return;
  const id = document.querySelector("#student-id").value;
  if (!window.confirm(`Delete student ${id}?`)) return;

  try {
    const response = await fetch(`${API_URL}/students/${id}`, { method: "DELETE" });
    if (!response.ok) throw new Error(await errorMessage(response));
    showMessage(`Student ${id} was deleted.`);
    idForm.reset();
  } catch (error) {
    showMessage(error.message || "Could not reach the API.", "error");
  }
});

showAllButton.addEventListener("click", async () => {
  showAllButton.disabled = true;
  showAllButton.textContent = "Loading...";

  try {
    const response = await fetch(`${API_URL}/students`);
    if (!response.ok) throw new Error(await errorMessage(response));

    const students = await response.json();
    studentsList.hidden = false;
    studentsList.className = "students-list";
    studentsList.replaceChildren();

    if (students.length === 0) {
      const emptyMessage = document.createElement("p");
      emptyMessage.textContent = "No students have been added yet.";
      studentsList.append(emptyMessage);
      return;
    }

    const list = document.createElement("ul");
    for (const student of students) {
      const item = document.createElement("li");
      item.textContent = `ID: ${student.id} · Name: ${student.name} · Age: ${student.age}`;
      list.append(item);
    }
    studentsList.append(list);
  } catch (error) {
    studentsList.hidden = false;
    studentsList.className = "students-list error";
    studentsList.replaceChildren();

    const errorText = document.createElement("p");
    errorText.textContent = error.message || "Could not reach the API.";
    studentsList.append(errorText);
  } finally {
    showAllButton.disabled = false;
    showAllButton.textContent = "Show all";
  }
});
  
