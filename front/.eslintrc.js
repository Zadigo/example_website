module.exports = {
    'root': true,
    'rules': {
        'no-console': 'off',
        'vue/max-attributes-per-line': ["error", {
            "singleline": {
                "max": 5
            },
            "multiline": {
                "max": 1
            }
        }],
        'vue/attributes-order': ["warning", {
            'alphabetical': false
        }]
    },
    "env": {
        "browser": true,
        "commonjs": true,
        "node": true,
        "es6": true,
    },
    "parser": "vue-eslint-parser",
    "parserOptions": {
        "parser": "babel-eslint",
        "ecmaVersion": 2018,
        "sourceType": "module",
        // "ecmaFeatures": {
        //     "jsx": true,
        //     "modules": true
        // }
    },
    'extends': [
        'eslint:recommended',
        'plugin:vue/recommended'
    ]
}
