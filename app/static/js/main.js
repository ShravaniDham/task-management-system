// Small client-side helpers: delete confirmation and title validation.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".delete-form").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      if (!window.confirm("Are you sure you want to delete this task?")) {
        event.preventDefault();
      }
    });
  });

  var addForm = document.getElementById("add-form");
  if (addForm) {
    addForm.addEventListener("submit", function (event) {
      var title = document.getElementById("title");
      if (title.value.trim() === "") {
        event.preventDefault();
        window.alert("Title is required.");
        title.focus();
      }
    });
  }
});
