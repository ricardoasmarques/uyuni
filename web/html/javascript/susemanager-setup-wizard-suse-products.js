$(function() {
  showProducts();

  // handles select all top/bottom checkboxes
  $("input.select-all").change(function() {
    $("#suse-products input[type='checkbox']:enabled").prop("checked", $(this).is(":checked"));
  });

  // handles expand/collapse buttons and text
  $(".table-content").on("click", ".collapsible", function() {
    var row = $(this).closest("tr");
    toggleExpansion(false, row);
  });

  // handles clicks on product checkboxes
  $(".table-content").on("change", "input", function(event) {
    var checked = $(this).prop("checked");
    var disabled = $(this).prop("disabled");
    var row = $(this).closest("tr");
    var productIdent = row.data("ident");
    var baseProductIdent = row.data("baseproductident");
    var base = baseProductIdent === "";

    if (base) {
      // Enable/disable sync buttons for addon products
      toggleAddonSyncButtons(productIdent, !(checked && disabled));
    }
    if (!checked && base) {
      $("tr[data-baseproductident='" + productIdent + "']")
        .find("input")
        .prop("checked", false);
    }
    if (checked && !base) {
      $("tr[data-ident='" + baseProductIdent + "']")
        .find("input")
        .prop("checked", true);
    }
    if (checked && base) {
      toggleExpansion(true, row);
    }
  });

  // handles synchronize bottom button
  $("#synchronize").click(function() {
    var checkboxes = $(".table-content input[type='checkbox']:checked:enabled");
    triggerProductSync(checkboxes);
  });

  // Handle clicks for "Add this product"
  function addProductButtonClickHandler() {
    var checkbox = $(this).closest('tr').find('input:checkbox');
    triggerProductSync(checkbox);
  }

  // Trigger product sync for a given array of checkboxes server side
  function triggerProductSync(checkboxes) {
    var idents = checkboxes.closest("tr").map(function() {
      return $(this).data("ident");
    }).toArray();

    var button = $("#synchronize");
    var icon = button.find("i");
    button.prop("disabled", true);
    icon.removeClass("fa-download");
    icon.addClass("fa-spinner");
    icon.addClass("fa-spin");

    ProductSyncAction.synchronize(idents, makeAjaxHandler(function() {
      $.each(checkboxes, function() {
        $(this).prop("checked", true);
        $(this).prop("disabled", true).trigger("change");

        $.each($(this).closest("tr").find("span.product-status"), function () {
          var status = $(this).data("syncstatus");
          if (status === "in_progress") {
            $(this).show();
          } else {
            $(this).hide();
          }
        });
      });

      icon.removeClass("fa-spin");
      icon.removeClass("fa-spinner");
      icon.addClass("fa-download");
      button.prop("disabled", false);
    }));
  }

  // Get the products or show message in case of errors
  function showProducts() {
    ProductsRenderer.renderAsync(makeAjaxHandler(
      function(content) {
        $("#loading-placeholder").hide();
        $(".table-content").append(content);
        $('.product-add-btn').tooltip();
        $('.product-add-btn').click(addProductButtonClickHandler);
        $('.product-channels-modal').modal({show: false});
        initSyncButtons();
      },
      function(message, exception) {
        $('.table').hide();
        if (exception.javaClassName.indexOf("InvalidMirrorCredentialException") > 0) {
          $("#invalid-credentials-alert-popup").show();
        } else if (exception.javaClassName.indexOf("ConnectionException") > 0) {
          $("#no-connection-alert-popup").show();
        } else {
          showFatalError();
        }
      })
    );
  }

  // Initially enable/disable sync buttons for addon products
  function initSyncButtons() {
    $("input[type='checkbox'].select-single").each(function() {
      var row = $(this).closest("tr");
      var baseProductIdent = row.data("baseproductident");
      var base = baseProductIdent === "";

      if (base) {
        var productIdent = row.data("ident");
        var checked = $(this).prop("checked");
        var disabled = $(this).prop("disabled");
        toggleAddonSyncButtons(productIdent, !(checked && disabled));
      }
    });
  }

  // Toggle sync buttons for addons of a given base product
  function toggleAddonSyncButtons(baseProductIdent, disabled) {
    $("tr[data-baseproductident='" + baseProductIdent + "']")
      .find("button.product-add-btn")
      .prop("disabled", disabled);
  }

  // expands or collapses a row, expects $(this) to point to an element
  // that is a descendant of a row.
  // Use forceExpand to force expansion (never collapse)
  function toggleExpansion(forceExpand, row) {
    var expandButton = row.find(".expand-button");
    var collapseButton = row.find(".collapse-button");
    var addonRows = $("tr[data-baseproductident='" + row.data("ident") + "']");

    if (forceExpand) {
      expandButton.hide();
      collapseButton.show();
      addonRows.show();
    } else {
      expandButton.toggle();
      collapseButton.toggle();
      addonRows.toggle();
    }
  }
});
