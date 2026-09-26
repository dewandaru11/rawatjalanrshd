document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  const filter = document.getElementById("filterInput");
  const table = document.getElementById("dataTable");
  if (filter && table) {
    filter.addEventListener("input", () => {
      const query = filter.value.toLowerCase().trim();
      table.querySelectorAll("tbody tr").forEach(row => {
        row.hidden = !row.textContent.toLowerCase().includes(query);
      });
    });
  }
});
