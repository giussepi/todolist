var app = app || {};

app.Todo = Backbone.Model.extend({

    defaults: {
	title: 'New todo',
	completed: false
    },

    toggle: function(){
	this.save({
	    completed: !this.get('completed')
	});
    }

});