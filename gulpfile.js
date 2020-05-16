/*jshint esversion: 6 */
/* jshint node: true */
const gulp = require('gulp');
const workboxBuild = require('workbox-build');
const htmlmin = require('gulp-htmlmin');
const concatCss = require('gulp-concat-css');
const concatJS = require('gulp-concat');
const cleanCSS = require('gulp-clean-css');
const uglify = require('gulp-uglify');
const pump = require('pump');
let djangoBlockCondition=/{%(.*?)%}/;
let djangoVariableCondition=/{{(.*?)}}/;
let ampImgCondition=/<amp-img([\s\S]*?)amp-img>/;
let ampCarouselCondition=/<amp-carousel([\s\S]*?)amp-carousel>/;

gulp.task('coreMinifyHtml', function() {
  return gulp.src('core/templates/core/dev/*.html')
    .pipe(htmlmin({collapseWhitespace: true, minifyJS: true, minifyCSS: true, removeComments: true, continueOnParseError: true, ignoreCustomFragments:[djangoBlockCondition,djangoVariableCondition,ampImgCondition,ampCarouselCondition]}))
    .pipe(gulp.dest('core/templates/core/prod'));
});

gulp.task('catalogMinifyHtml', function() {
  return gulp.src('catalog/templates/catalog/dev/*.html')
    .pipe(htmlmin({collapseWhitespace: true, minifyJS: true, minifyCSS: true, removeComments: true, ignoreCustomFragments:[djangoBlockCondition,djangoVariableCondition,ampImgCondition,ampCarouselCondition]}))
    .pipe(gulp.dest('catalog/templates/catalog/prod'));
});

gulp.task('conditionsMinifyHtml', function() {
  return gulp.src('conditions/templates/conditions/dev/*.html')
    .pipe(htmlmin({collapseWhitespace: true, minifyJS: true, minifyCSS: true, removeComments: true, ignoreCustomFragments:[djangoBlockCondition,djangoVariableCondition,ampImgCondition,ampCarouselCondition]}))
    .pipe(gulp.dest('conditions/templates/conditions/prod'));
});

gulp.task('contactsMinifyHtml', function() {
  return gulp.src('contacts/templates/contacts/dev/*.html')
    .pipe(htmlmin({collapseWhitespace: true, minifyJS: true, minifyCSS: true, removeComments: true, ignoreCustomFragments:[djangoBlockCondition,djangoVariableCondition,ampImgCondition,ampCarouselCondition]}))
    .pipe(gulp.dest('contacts/templates/contacts/prod/'));
});

gulp.task('formsMinifyHtml', function() {
  return gulp.src('forms/templates/forms/dev/*.html')
    .pipe(htmlmin({collapseWhitespace: true, minifyJS: true, minifyCSS: true, removeComments: true, ignoreCustomFragments:[djangoBlockCondition,djangoVariableCondition,ampImgCondition,ampCarouselCondition]}))
    .pipe(gulp.dest('forms/templates/forms/prod/'));
});

gulp.task('сitiesMinifyHtml', function() {
  return gulp.src('cities/templates/cities/dev/*.html')
    .pipe(htmlmin({collapseWhitespace: true, minifyJS: true, minifyCSS: true, removeComments: true, ignoreCustomFragments:[djangoBlockCondition,djangoVariableCondition,ampImgCondition,ampCarouselCondition]}))
    .pipe(gulp.dest('cities/templates/cities/prod/'));
});

gulp.task('createBaseCSS', function () {
  return gulp.src(['core/static/core/plugins/vendor/slicknav/slicknav.min.css', 'core/static/core/css/dev/style.css','core/static/core/plugins/vendor/bootstrap4/bootstrap.min.css'])
    .pipe(concatCss("prod-style.css"))
    .pipe(cleanCSS())
    .pipe(gulp.dest('core/static/core/css/prod/'));
});

gulp.task('createNewBaseCSS', function () {
  return gulp.src(['core/static/core/css/dev/newdesign-base.css', 'core/static/core/css/dev/newdesign-576.css', 'core/static/core/css/dev/newdesign-768.css', 'core/static/core/css/dev/newdesign-992.css'])
    .pipe(concatCss("prod-style-newdesign.css"))
    .pipe(cleanCSS())
    .pipe(gulp.dest('core/static/core/css/prod/'));
});

gulp.task('concatBaseJS', function() {
  return gulp.src(['core/static/core/plugins/vendor/jquery-2.2.4.min.js','core/static/core/plugins/vendor/tether.min.js','core/static/core/plugins/vendor/bootstrap4/bootstrap.min.js', 'core/static/core/plugins/vendor/slicknav/jquery.slicknav.min.js'])
    .pipe(concatJS('base.js'))
    .pipe(gulp.dest('core/static/core/plugins/dev/'));
});

gulp.task('compressBaseJS', function (cb) {
  pump([
        gulp.src('core/static/core/plugins/dev/base.js'),
        uglify(),
        gulp.dest('core/static/core/plugins/prod/')
    ],
    cb
  );
});

gulp.task('concatMainJS', function() {
  return gulp.src(['core/static/core/plugins/react/bundle-prod.js','core/static/core/plugins/vendor/jquery.drawsvg.js', 'core/static/core/plugins/vendor/parallax/parallaxie.js'])
    .pipe(concatJS('main.js'))
    .pipe(gulp.dest('core/static/core/plugins/dev/'));
});

gulp.task('compressMainJS', function (cb) {
  pump([
        gulp.src('core/static/core/plugins/dev/main.js'),
        uglify(),
        gulp.dest('core/static/core/plugins/prod/')
    ],
    cb
  );
});

gulp.task('service-worker', () => {
  return workboxBuild.injectManifest({
	globDirectory: '/var/www/vekokat.ru/',
    swSrc: '/var/www/vekokat.ru/vekokat_ver2/core/templates/core/serviceWorker/sw-dev.js',
    swDest: '/var/www/vekokat.ru/vekokat_ver2/core/templates/core/serviceWorker/sw.js',
    globPatterns: ['**/*.{html,js,css,jpg,png,ttf,otf}'],
    globIgnores: ['media\/**','VekokatNew\/**','core\/**','static/admin\/**',
          'static/ckeditor\/**','static/jet\/**','vekokat_ver2\/**',
          'static/jet.dashboard\/**','static/range_filter\/**','static/rest_framework\/**', 'static/core/css/dev\/**', 'static/core/css/images\/**', 'static/core/images\/**', 'static/core/plugins/vendor\/**', 'static/core/plugins/dev\/**'],
  }).then(({count, size, warnings}) => {
    // Optionally, log any warnings and details.
    warnings.forEach(console.warn);
    console.log(`${count} files will be precached, totaling ${size} bytes.`);
  });
});

gulp.task('minifyHtml', gulp.parallel('catalogMinifyHtml', 'conditionsMinifyHtml', 'contactsMinifyHtml', 'formsMinifyHtml', 'сitiesMinifyHtml'));