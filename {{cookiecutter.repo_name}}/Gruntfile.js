module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    less: {
      development: {
        files: {
          "{{ cookiecutter.repo_name }}/static/style/css/theme-default.css": "{{ cookiecutter.repo_name }}/static/style/less/main.less"
        }
      }
    },
    watch: {
      files: ['{{ cookiecutter.repo_name }}/static/style/less/**/*.less'],
      tasks: ['less'],
      options: {
        livereload: true
      }
    },
    cssmin: {
        minify: {
            files: {
                "{{ cookiecutter.repo_name }}/static/style/css/theme-default.min.css": "{{ cookiecutter.repo_name }}/static/style/css/theme-default.css"
            }
        }
    },
    img: {
        optimize: {
            src: '{{ cookiecutter.repo_name }}/static/img'
        }
    },
    watch: {
      files: ['{{ cookiecutter.repo_name }}/static/style/less/*.less'],
      tasks: ['less', 'cssmin'],
      options: {
        livereload: true
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-img');

  grunt.registerTask('default', ['less']);

};