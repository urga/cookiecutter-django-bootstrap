module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    less: {
      development: {
        files: {
          "{{ cookiecutter.repo_name }}/static/style/css/theme-default.css": "{{ cookiecutter.repo_name }}/static/style/less/theme-default.less"
        }
      }
    },
    watch: {
      files: ['{{ cookiecutter.repo_name }}/static/style/less/**/*.less'],
      tasks: ['less'],
      options: {
        livereload: true
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['less']);

};