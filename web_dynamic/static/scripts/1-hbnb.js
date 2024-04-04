document.addEventListener('DOMContentLoaded', function () {
  let disObjs = {};
  let $h4 = $('div.amenities h4');

  $('input').each(function (idx, ele) {
    let id = $(this).attr('data-id');
    let name = $(this).attr('data-name');

    disObjs[id] = {name: name, checked: false};

    $(ele).change(function () {
      let delim = '<span class="delim">, </span>';
      $('h4 span.delim').remove();

      if (this.checked) {
        console.log('checked');
        disObjs[id]['checked'] = true;
        $h4.append('<span id=' + id + '>' + name + '</span>');
      } else {
        console.log('unchecked');
        disObjs[id]['checked'] = false;
        $('span#' + id).remove();
      }

      let length = $('h4 > span').length;
      console.log($('h4 > span').length);
      $('div.amenities h4 span').each(function (idx, ele) {
        if (idx < length - 1) {
          $(this).append(delim);
        }
      });
    });
  });
});
