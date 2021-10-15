const { defaults } = require('jest-config')

module.exports = {
    "verbose": true,
    "roots": ["<rootDir>/src/", "<rootDir>/tests/unit/"],
    "moduleFileExtensions": ["js", "vue"],
    "transform": {
        ".*\\.(vue)$": "vue-jest"
    },
    "snapshotSerializers": defaults.snapshotSerializers,
    "testURL": "http://localhost/"
}
