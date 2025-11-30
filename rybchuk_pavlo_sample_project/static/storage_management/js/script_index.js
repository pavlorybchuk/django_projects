"use strict";

document.addEventListener("DOMContentLoaded", function () {
  const change_buttons = document.querySelectorAll(".change-btn");
  const delete_buttons = document.querySelectorAll(".del-btn");
  const aside_trigger = document.querySelector("#aside_trigger");
  const change_modal = document.querySelector("#change_modal");
  const delete_modal = document.querySelector("#delete_modal");
  const urlTemplateChange = change_modal.querySelector("#change-form").action;
  const urlTemplateDelete = delete_modal.querySelector("#delete-form").action;
  const change_form = change_modal.querySelector("#change-form");

  change_buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const row = button.closest("tr");
      const prod_id = button.dataset.prodId;
      const name = row.firstElementChild.nextElementSibling;
      const age_category = name.nextElementSibling.nextElementSibling;
      const material = age_category.nextElementSibling;
      const brand = material.nextElementSibling;
      const price = brand.nextElementSibling;
      const urlParts = urlTemplateChange.split("/");
      urlParts[urlParts.length - 2] = prod_id;
      const url = urlParts.join("/");
      change_form.action = url;

      change_form.querySelector("#prod_id").value = prod_id;
      change_form.querySelector("#name").value = name.textContent;
      change_form.querySelector("#age_category").value =
        age_category.textContent;
      change_form.querySelector("#material").value = material.textContent;
      change_form.querySelector("#brand").value = brand.textContent;
      change_form.querySelector("#price").value = price.textContent;
      aside_trigger.classList.remove("hidden");
      change_modal.classList.remove("hidden");
    });
  });

  delete_buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const del_prod_id = this.dataset.prodId;
      console.log(del_prod_id)
      const urlParts = urlTemplateDelete.split("/");
      urlParts[urlParts.length - 2] = del_prod_id;
      const url = urlParts.join("/");
      delete_modal.querySelector("#delete-form").action = url;
      delete_modal.querySelector("#del_prod_id").value = del_prod_id;
      aside_trigger.classList.remove("hidden");
      delete_modal.classList.remove("hidden");
    });
  });

  aside_trigger.addEventListener("click", function (e) {
    e.preventDefault();
    aside_trigger.classList.add("hidden");
    delete_modal.classList.add("hidden");
  });

  delete_modal
    .querySelector("#close-delete-modal")
    .addEventListener("click", function (e) {
      e.preventDefault();
      aside_trigger.classList.add("hidden");
      delete_modal.classList.add("hidden");
    });

  change_modal
    .querySelector("#close-modal")
    .addEventListener("click", function (e) {
      e.preventDefault();
      aside_trigger.classList.add("hidden");
      change_modal.classList.add("hidden");
    });
});
