from .common import BASE_DIR
import os

PIPELINE = {
    'COMPILERS': (
        'pipeline.compilers.less.LessCompiler',
    ),
    'LESS_BINARY': os.path.join(BASE_DIR, '..', 'node_modules/.bin/lessc'),
    'STYLESHEETS': {
        'libs': {
            'source_filenames': (
                'vendor/bootstrap/css/bootstrap.css',
                'css/bootstrap-theme.css'
            ),
            'output_filename': 'css/libs.css'
        },
        'index': {
            'source_filenames': (
                'css/index.less',
            ),
            'output_filename': 'css/index.css'
        }
    },
    'JAVASCRIPT': {
        'libs': {
            'source_filenames': (
                'vendor/jquery/jquery-2.1.4.js',
                'vendor/bootstrap/js/bootstrap.js',
                'vendor/trianglify/trianglify.min.js'
            ),
            'output_filename': 'js/libs.js'
        },
        'index': {
            'source_filenames': (
                'js/index.js',
            ),
            'output_filename': 'js/index.js'
        }
    }
}
