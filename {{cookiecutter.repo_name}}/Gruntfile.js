module.exports = function(grunt) {

grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    less: {
        development: {
            files: {
                "{{ cookiecutter.repo_name }}/static/css/theme-default.css": "{{ cookiecutter.repo_name }}/static/less/theme-default.less"
            }
        }
    },
    cssmin: {
        minify: {
            files: {
                "{{ cookiecutter.repo_name }}/static/css/theme-default.min.css": "{{ cookiecutter.repo_name }}/static/css/theme-default.css"
            }
        }
    },
    img: {
        optimize: {
            src: '{{ cookiecutter.repo_name }}/static/img'
        }
    },
    watch: {
        less: {
            files: ['{{ cookiecutter.repo_name }}/static/less/**/*.less'],
            tasks: ['less', 'cssmin'],
            options: {
                livereload: true
            }
        },
        img: {
            files: ['{{ cookiecutter.repo_name }}/static/img/**/*'],
            tasks: ['img']
        }
    }
 });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-img');

  grunt.registerTask('default', ['less', 'cssmin']);

};