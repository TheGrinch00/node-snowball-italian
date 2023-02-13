{
    "targets": [
        {
            "target_name": "snowball",
            "include_dirs" : [ 
                "<!(node -e \"require('nan')\")"
            ],
            "sources": [
                "src/snowball.cpp",
                "src/NativeExtension.cpp",
                "src/libstemmer/libstemmer/libstemmer.c",
                "src/libstemmer/runtime/api.c",
                "src/libstemmer/runtime/utilities.c",
                "src/libstemmer/src_c/stem_ISO_8859_1_italian.c",
                "src/libstemmer/src_c/stem_UTF_8_italian.c"
            ]
        }
    ]
}