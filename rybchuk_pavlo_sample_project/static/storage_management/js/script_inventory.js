document.addEventListener("DOMContentLoaded", () => {
  const aside_trigger = document.getElementById("aside_trigger");
  const change_modal = document.getElementById("change_modal");
  const rec_id_input = document.getElementById("rec_id");

  const qty_input = document.getElementById("quantity");
  const min_req_input = document.getElementById("min_required");

  const change_buttons = document.querySelectorAll(".change-btn");

  change_buttons.forEach((btn) => {
    btn.addEventListener("click", async () => {
      const recId = btn.dataset.recId;
      rec_id_input.value = recId;
      const row = btn.closest("tr");
      const min_required = row.lastElementChild.previousElementSibling.previousElementSibling;
      const quantity = min_required.previousElementSibling;
      qty_input.value = quantity.textContent;
      min_req_input.value = min_required.textContent;
      aside_trigger.classList.remove("hidden");
      change_modal.classList.remove("hidden");
    });
  });

  document.getElementById("close-modal").addEventListener("click", () => {
    change_modal.classList.add("hidden");
    aside_trigger.classList.add("hidden");
  });

  const delete_modal = document.getElementById("delete_modal");
  const del_id_input = document.getElementById("del_rec_id");
  const delete_buttons = document.querySelectorAll(".del-btn");

  delete_buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const del_prod_id = this.dataset.recId;
      del_id_input.value = del_prod_id;
      aside_trigger.classList.remove("hidden");
      delete_modal.classList.remove("hidden");
    });
  });

  document
    .getElementById("close-delete-modal")
    .addEventListener("click", () => {
      delete_modal.classList.add("hidden");
      aside_trigger.classList.add("hidden");
    });
  aside_trigger.addEventListener("click", () => {
    delete_modal.classList.add("hidden");
    aside_trigger.classList.add("hidden");
  });
});
