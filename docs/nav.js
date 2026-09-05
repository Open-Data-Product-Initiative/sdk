(function () {
  var sidebar = document.querySelector(".sidebar");
  var toggle = document.querySelector(".mobile-nav-toggle");
  var nav = document.querySelector("#docs-nav");

  if (!sidebar || !toggle || !nav) {
    return;
  }

  function setOpen(open) {
    sidebar.setAttribute("data-open", open ? "true" : "false");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  function scrollToHash() {
    if (!window.location.hash) {
      return;
    }

    var target = document.getElementById(window.location.hash.slice(1));
    if (target) {
      window.scrollTo({ top: target.offsetTop, behavior: "instant" });
    }
  }

  function scheduleHashScroll() {
    window.setTimeout(scrollToHash, 0);
    window.setTimeout(scrollToHash, 120);
    window.setTimeout(scrollToHash, 360);
  }

  sidebar.setAttribute("data-menu-ready", "true");
  setOpen(false);
  scheduleHashScroll();

  toggle.addEventListener("click", function () {
    setOpen(sidebar.getAttribute("data-open") !== "true");
  });

  nav.addEventListener("click", function (event) {
    var link = event.target.closest("a");
    if (!link) {
      return;
    }

    if (window.matchMedia("(max-width: 920px)").matches) {
      setOpen(false);
    }

    if (link.hash && link.pathname === window.location.pathname) {
      scheduleHashScroll();
    }
  });
})();
