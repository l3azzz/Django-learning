// AJAX handler for demo request form
// Uses jQuery and SweetAlert2

(function () {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const csrftoken = getCookie("csrftoken");

  $(document).ready(function () {
    $("#demo-request-form").on("submit", function (e) {
      e.preventDefault();
      const email = $("#demo-email").val().trim();
      if (!email) {
        Swal.fire({
          icon: "warning",
          title: "Email required",
          text: "Please enter your work email.",
        });
        return;
      }

      // Show loading
      Swal.fire({
        title: "Sending request...",
        allowOutsideClick: false,
        didOpen: () => {
          Swal.showLoading();
        },
      });

      $.ajax({
        url: "/api/demo-request/",
        method: "POST",
        data: { email: email },
        beforeSend: function (xhr) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
      })
        .done(function (resp) {
          Swal.close();
          if (resp.status === "ok") {
            Swal.fire({
              icon: "success",
              title: "Request received",
              text: resp.message || "We will contact you soon.",
            });
            $("#demo-email").val("");
          } else if (resp.status === "exists") {
            Swal.fire({
              icon: "info",
              title: "Already registered",
              text: resp.message || "You already requested a demo.",
            });
          } else if (resp.status === "saved_email_failed") {
            Swal.fire({
              icon: "warning",
              title: "Saved but email failed",
              text: resp.message || "Saved but sending confirmation failed.",
            });
          } else {
            Swal.fire({
              icon: "error",
              title: "Error",
              text: resp.message || "Something went wrong.",
            });
          }
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
          Swal.close();
          let msg = "Request failed. Try again.";
          try {
            const json = jqXHR.responseJSON;
            if (json && json.message) msg = json.message;
          } catch (e) {}
          Swal.fire({
            icon: "error",
            title: "Error",
            text: msg,
          });
        });
    });
  });
})();
