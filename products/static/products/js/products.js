/**
* @fileOverview Products JavaScript Function Library.
* @author <a href="https://github.com/richardhenyash">Richard Ash</a>
* @version 1.1.1
*/
/*jshint esversion: 6 */
/* globals $, buildConfirmModal, buildInformationModal */

/* Set product rating stars for all divs with the class product-rating-stars */
/* Note - reads the product rating from the product-rating data attribute */
$('.product-rating-stars').each(function () {
    let productRating = $(this).data("product-rating");
    if ((productRating == "None") || (productRating == null) || (productRating == ""))
        $(this).html("<i class=rating-text>Not Rated</i>");
    else {
        let productRatingRounded = (Math.round(productRating));
        let stars = $(this).children();
        stars.each(function(si) {
            if (productRatingRounded > si) {
                $(this).addClass("fg-yellow");
            }
        });
    }
});

/* On click event handlers added to product review edit stars */
/* Note, updates the hidden form input rating with the selected rating */
$('.product-review-edit-stars').each(function () {
    let currentRating = $(this).data("product-rating");
    let stars = $(this).children();
    stars.each(function(si) {
        if (currentRating > si) {
            $(this).addClass("fg-yellow");
        }
        $(this).click(function() {
            let starId = $(this).attr('id');
            let rating = parseInt(starId.slice(-1));
            colourStars(rating, "#star-");
        });
    });
});

// On click event handler added to product image link to build modal dialog
$("#productInformationImgLink").click(function() {
    (buildInformationModal("#productInformationImgLink", "information-modal-title", "#product-description-array", "#informationModal", "modal-lg"));
});

// On click event handler added to product information button to build modal dialog
$("#productInformationBtn").click(function() {
    (buildInformationModal("#productInformationBtn", "information-modal-title", "#product-description-array", "#informationModal", "modal-xl"));
});

// On click event handler added to size information button to build modal dialog
$("#sizeInformationBtn").click(function() {
    (buildInformationModal("#sizeInformationBtn", "information-modal-title", "#size-information-array", "#informationModal", "modal-sm"));
});

// On click event handler added to type information button to build modal dialog
$("#typeInformationBtn").click(function() {
    (buildInformationModal("#typeInformationBtn", "information-modal-title", "#type-information-array", "#informationModal", ""));
});

// On click event handler added to create plan button to build modal dialog
$("#createPlanBtn").click(function() {
    (buildInformationModal("#createPlanBtn", "information-modal-title", null, "#informationModal", "modal-sm"));
});


// On click event handler added to product delete button to build delete confirmation modal dialog
$("#productDeleteBtn").click(function() {
    (buildConfirmModal("#productDeleteBtn", "#confirmModal"));
});

// On click event handler added to review delete buttons to build delete confirmation modal dialog
$('.reviewDeleteBtn').each(function () {
    let btnId = "#" + $(this).attr("id");
    $(btnId).click(function() {
        (buildConfirmModal(btnId, "#confirmModal"));
    });
});

// On click event handler added to minus button to decrease product quantity and update price
$("#product-quantity-minus-btn").click(function() {
    (incrementQuantity("#product-quantity", "#product-quantity-minus-btn", "#product-quantity-plus-btn", -1, 1, 99));
    (setPriceBasedOnSizeAndQuantity("#product-size", "#product-quantity", "#product-price-dict", '#product-price'));
});

// On click event handler added to plus button to decrease product quantity and update price
$("#product-quantity-plus-btn").click(function() {
    (incrementQuantity("#product-quantity", "#product-quantity-minus-btn", "#product-quantity-plus-btn", 1, 1, 99));
    (setPriceBasedOnSizeAndQuantity("#product-size", "#product-quantity", "#product-price-dict", '#product-price'));
});

// On change event handler added to size selector to update price
$("#product-size").change(function() {
    (setPriceBasedOnSizeAndQuantity("#product-size", "#product-quantity", "#product-price-dict", '#product-price'));
});

// On change event handler added to size selector to update price
$('#id_size').change(function() {
    setPriceBasedOnSize("#id_size :selected", "#product-price-dict", "#id_price");
});

// On change event handler added to image in custom clearable file input
// Displays new file name
$('#new_image').change(function() {
    let file = $('#new_image')[0].files[0];
    $('#filename_image').text(`Image will be set to: ${file.name}`);
});

// On change event handler added to alternate image in custom clearable file input
// Displays new file name
$('#new_image_alt').change(function() {
    let file = $('#new_image_alt')[0].files[0];
    $('#filename_image_alt').text(`Image will be set to: ${file.name}`);
});

/**
* [Function to add yellow colour class to stars]
* @return {[rating]}                     [rating, integer]          
*/
function colourStars(rating, starIdPrefix) {

    // Remove yellow class from all rating stars
    for (let i = 1; i <= 5; i++) {
        $(starIdPrefix + i).removeClass("fg-yellow");
    }
    // Add yellow class to correct rating stars
    for (let i = 1; i <= rating; i++) {
        $(starIdPrefix + i).addClass("fg-yellow");
    }
    $('input[name=rating]').val(rating);
    return rating;
}

/**
* [Function to increment product quantities given quantityId, positive or negative increment, minimum value and maximum value]
* @return {[newQuantity]}                     [New Quantity, string]          
*/
function incrementQuantity(quantityId, btnMinusID, btnPlusID, inc, minValue, maxValue){
    let currentQuantity = parseInt($(quantityId).val());
    let newQuantity = currentQuantity;
    if (Math.sign(inc) == 1) {
        if ((currentQuantity + inc) <= maxValue) {
            newQuantity = currentQuantity + inc;
        }
    } else {
        if ((currentQuantity + inc) >= minValue) {
            newQuantity = currentQuantity + inc;
        }            
    }
    if (newQuantity != currentQuantity) {
        $(quantityId).val(newQuantity);
    }
    if (newQuantity <= minValue) {
        $(btnMinusID).attr("disabled", true);
    } else {
        $(btnMinusID).removeAttr('disabled');
    }
    if (newQuantity >= maxValue) {
        $(btnPlusID).attr("disabled", true);
    } else {
        $(btnPlusID).removeAttr('disabled');
    }
    return newQuantity;
}

/**
* [Function to set price based on size selected]
* @return {[priceStr]}                     [price, string]          
*/
function setPriceBasedOnSize(sizeId, scriptId, priceId) {
    let size = $(sizeId).text();
    let priceDict = JSON.parse($(scriptId).text());
    let priceStr = priceDict[size];
    $(priceId).val(priceStr);
    return priceStr;
}

/**
* [Function to set price based on size and quantity selected]
* @return {[priceStr]}                     [price, string]          
*/
function setPriceBasedOnSizeAndQuantity(sizeId, quantityId, scriptId, priceId) {
    let size = $(sizeId).val();
    let quantity = parseInt($(quantityId).val());
    // Get price object
    let priceDict = JSON.parse($(scriptId).text());
    let price = priceDict[size];
    let priceStr = ("£" + (price * quantity).toFixed(2));
    $(priceId).text(priceStr);
    return priceStr;
}