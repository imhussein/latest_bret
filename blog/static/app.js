window.addEventListener("load", () => {
  document.getElementById("logout_link").addEventListener("click", (e) => {
    e.preventDefault();
    const form = document.getElementById("logout");
    form.submit();
  });
});
