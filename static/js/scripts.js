/*!
    * Start Bootstrap - Freelancer v6.0.5 (https://startbootstrap.com/theme/freelancer)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
    */
    (function($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
      if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          $('html, body').animate({
            scrollTop: (target.offset().top - 71)
          }, 1000, "easeInOutExpo");
          return false;
        }
      }
    });

    // Scroll to top button appear
    $(document).scroll(function() {
      var scrollDistance = $(this).scrollTop();
      if (scrollDistance > 100) {
        $('.scroll-to-top').fadeIn();
      } else {
        $('.scroll-to-top').fadeOut();
      }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function() {
      $('.navbar-collapse').collapse('hide');
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
      target: '#mainNav',
      offset: 80
    });

    // Collapse Navbar
    var navbarCollapse = function() {
      if ($("#mainNav").offset().top > 100) {Please
        $("#mainNav").addClass("navbar-shrink");
      } else {
        $("#mainNav").removeClass("navbar-shrink");
      }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);

    // Floating label headings for the contact form
    $(function() {
      $("body").on("input propertychange", ".floating-label-form-group", function(e) {
        $(this).toggleClass("floating-label-form-group-with-value", !!$(e.target).val());
      }).on("focus", ".floating-label-form-group", function() {
        $(this).addClass("floating-label-form-group-with-focus");
      }).on("blur", ".floating-label-form-group", function() {
        $(this).removeClass("floating-label-form-group-with-focus");
      });
    });

  })(jQuery); // End of use strict
//functions to add extra paragraphs to blog form
function addParagraphToBlog() {
  var new_chq_no = parseInt($('#total_chq').val()) + 1;
  var new_input = "<div class='form-group' id='blogParagraph" + new_chq_no +"'><label for='inputParagraphBlog'>Paragraph " + new_chq_no + "</label><textarea class='form-control' name='inputParagraphBlog" + new_chq_no + "' id='inputParagraphBlog" + new_chq_no + "'></textarea></div>";
  if (new_chq_no <= 12) {
    $('#new_paragraph').append(new_input);
    $('#total_chq').val(new_chq_no);
    }
  else {
    $.notifyBar({ cssClass: "error", html: "Error: maximum 12 paragraphs are allowed" });
    }
  }

//functions to remove extra paragraphs from blog form
function removeParagraphToBlog() {
  var last_chq_no = $('#total_chq').val();
  if (last_chq_no > 1) {
    $('#blogParagraph' + last_chq_no).remove();
    $('#total_chq').val(last_chq_no - 1);
  }
}
//functions to add extra paragraphs from project form
function addParagraphToProject() {
  var new_chq_no = parseInt($('#total_chq1').val()) + 1;
  var new_input = "<div class='form-group' id='projectParagraph" + new_chq_no +"'><label for='inputParagraphProject'>Paragraph " + new_chq_no + "</label><textarea class='form-control' name='inputParagraphProject" + new_chq_no + "' id='inputParagraphProject" + new_chq_no + "'></textarea></div>";
  if (new_chq_no <= 12) {
    $('#new_paragraph1').append(new_input);
    $('#total_chq1').val(new_chq_no);
    }
  else {
    $.notifyBar({ cssClass: "error", html: "Error: maximum 12 paragraphs are allowed" });
    }
  }

//functions to remove extra paragraphs from project form
function removeParagraphToProject() {
  var last_chq_no = $('#total_chq1').val();
  if (last_chq_no > 1) {
    $('#projectParagraph' + last_chq_no).remove();
    $('#total_chq1').val(last_chq_no - 1);
  }
}

//function to display the files that are selected in a form
$(function() {
    // Multiple images preview in browser
    var imagesPreview = function(input, placeToInsertImagePreview) {

        if (input.files) {
            var filesAmount = input.files.length;
            for (i = 0; i < filesAmount; i++) {
                var reader = new FileReader();
                reader.onload = function(event) {
                    $($.parseHTML('<img>')).attr('src', event.target.result).appendTo(placeToInsertImagePreview);

                }

                reader.readAsDataURL(input.files[i]);
            }
        }

    };

    $('#files').on('change', function() {
        imagesPreview(this, 'div.gallery');
    });
});


//$("#common").click(function () {
//$.notifyBar();
//});
//$("#error").click(function () {
//$.notifyBar({ cssClass: "error", html: "Error occurred!" });
//});

//Send admin_blog_form through AJAX


