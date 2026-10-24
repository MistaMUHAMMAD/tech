"use strict";
document.documentElement.classList.add("js");

const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#site-nav");
function closeMenu(returnFocus = false) {
  if (!menuButton || !navigation) return;
  navigation.classList.remove("is-open");
  menuButton.setAttribute("aria-expanded", "false");
  if (returnFocus) menuButton.focus();
}
if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const open = menuButton.getAttribute("aria-expanded") !== "true";
    menuButton.setAttribute("aria-expanded", String(open));
    navigation.classList.toggle("is-open", open);
  });
  navigation.querySelectorAll("a").forEach(link => link.addEventListener("click", () => closeMenu()));
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && navigation.classList.contains("is-open")) closeMenu(true);
  });
  document.addEventListener("click", event => {
    if (!event.target.closest(".site-header")) closeMenu();
  });
  window.addEventListener("resize", () => {
    if (window.innerWidth > 900) closeMenu();
  });
}

document.querySelectorAll("[data-year]").forEach(el => { el.textContent = String(new Date().getFullYear()); });

const emailButton = document.querySelector("[data-copy-email]");
if (emailButton) {
  emailButton.addEventListener("click", async () => {
    const status = document.querySelector("#copy-status");
    try {
      await navigator.clipboard.writeText("muhammad.musa4rl@gmail.com");
      status.textContent = "Email address copied.";
    } catch {
      status.textContent = "Copy this address: muhammad.musa4rl@gmail.com";
    }
  });
}

const form = document.querySelector("#contact-form");
if (form) {
  form.addEventListener("submit", event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const name = form.querySelector("#sender-name").value.trim();
    const email = form.querySelector("#sender-email").value.trim();
    const message = form.querySelector("#message").value.trim();
    if (!name || !email || !message) {
      document.querySelector("#form-status").textContent = "Please enter your name, email and message.";
      return;
    }
    const subject = `Portfolio enquiry from ${name}`;
    const body = `${message}\n\nFrom: ${name}\nReply email: ${email}`;
    const mailto = `mailto:muhammad.musa4rl@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    window.location.href = mailto;
    document.querySelector("#form-status").textContent = "Email draft requested. If your email app did not open, email muhammad.musa4rl@gmail.com directly. No message has been sent by this site.";
  });
  // Enable only after the local draft handler is ready. A mailto form action
  // is classified by Chrome as an insecure form target on HTTPS pages.
  form.querySelector('button[type="submit"]').disabled = false;
}

const filters = document.querySelector(".filter-bar");
if (filters) {
  filters.hidden = false;
  const cards = [...document.querySelectorAll(".sample-card")];
  const buttons = [...filters.querySelectorAll("[data-filter]")];
  buttons.forEach(button => button.addEventListener("click", () => {
    const category = button.dataset.filter;
    buttons.forEach(other => {
      const active = other === button;
      other.classList.toggle("active", active);
      other.setAttribute("aria-pressed", String(active));
    });
    let count = 0;
    cards.forEach(card => {
      const visible = category === "All" || card.dataset.category === category;
      card.hidden = !visible;
      if (visible) count++;
    });
    document.querySelector("#filter-status").textContent = `${count} ${count === 1 ? "sample" : "samples"} shown`;
  }));
}
