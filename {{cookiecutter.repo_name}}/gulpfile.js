'use strict';

var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var childProcess = require('child_process');
var browserSync = require('browser-sync');
var reload = browserSync.reload;

// Compile  stylesheets
gulp.task('styles', function () {
  // For best performance, don't add Sass partials to `gulp.src`
  return gulp.src([
    '{{ cookiecutter.repo_name }}/static/scss/main.scss'
  ])
    .pipe($.sourcemaps.init())
    //.pipe($.changed('{{ cookiecutter.repo_name }}/static/css', {extension: '.css'}))
    .pipe($.sass({
      precision: 10,
      onError: console.error.bind(console, 'Sass error:')
    }))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('{{ cookiecutter.repo_name }}/static/css'))
    // Concatenate and minify styles
    //.pipe($.if('*.css', $.csso()))
    //.pipe(gulp.dest('{{ cookiecutter.repo_name }}/static/css/min'))
    .pipe($.size({title: 'styles'}));
});

gulp.task('runserver', function() {
  var runserver;
  runserver = childProcess.exec('./manage.py runserver', function (error, stdout, stderr) {
    if (error) {
      console.log(error.stack);
      console.log('Error code: ' + error.code);
      console.log('Signal received: ' + error.signal);
    }
    console.log('runserver STDOUT: ' + stdout);
    console.log('runserver STDERR: ' + stderr);
  });

  runserver.on('exit', function (code) {
    console.log('Child process exited with exit code '+code);
  });
});

// Watch files for changes & reload
gulp.task('serve', ['styles', 'runserver'], function () {
  browserSync({
    notify: false,
    // Customize the BrowserSync console logging prefix
    logPrefix: 'EGICO',
    open: false,
    proxy: "127.0.0.1:8000"
  });

  //gulp.watch(['app/**/*.html'], reload);
  gulp.watch('*/templates/**/*.html', [reload]);
  gulp.watch(['{{ cookiecutter.repo_name }}/static/scss/**/*.{scss,css}'], ['styles', reload]);
});