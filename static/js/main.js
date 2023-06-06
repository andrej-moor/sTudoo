$(document).ready(function() {
    $('.add-class-btn').click(function() {
      $('.add-form').hide();
      $('form[name="add_class_form"]').show();
    });
  
    $('.add-project-btn').click(function() {
      $('.add-form').hide();
      $('form[name="add_project_form"]').show();
    });
  
    $('.add-todo-btn').click(function() {
      $('.add-form').hide();
      $('form[name="add_todo_form"]').show();
    });
  });
  