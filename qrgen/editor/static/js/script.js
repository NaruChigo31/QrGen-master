var image = new Image(); 
// важно добавить обработчик события до инициализации загрузки картинки
image.onload = function(){
   $('#img-tag')
      .css({'opacity':0, 'display':'none'})
      .attr('src', this.src)
      .fadeIn();
}
i.src = "{{ url.image.url }}"; // существующее изображение
