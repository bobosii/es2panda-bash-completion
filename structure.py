ast_checks = [
    "Base", "NodeHasParent", "NodeHasSourceRange", "EveryChildHasValidParent",
    "EveryChildInParentRange", "AfterPluginsAfterParse", "CheckStructDeclaration",
    "AfterScopesInitPhase", "VariableHasScope", "AfterCheckerPhase", "NodeHasType",
    "NoPrimitiveTypes", "IdentifierHasVariable", "ReferenceTypeAnnotationIsNull",
    "ArithmeticOperationValid", "SequenceExpressionHasLastType", "ForLoopCorrectlyInitialized",
    "VariableHasEnclosingScope", "ModifierAccessValid", "VariableNameIdentifierNameSame",
    "CheckAbstractMethod", "GetterSetterValidation", "CheckScopeDeclaration", "CheckConstProperties"
]
ets_checks = [
    "subset_aware", "ets-prohibit-top-level-statements", "ets-boost-equality-statement",
    "ets-remove-lambda", "ets-implicit-boxing-unboxing", "ets-annotation-unused-generic-alias-warn",
    "subset_unaware", "ets-suggest-final", "ets-remove-async"
]

options = {
    "--arktsconfig": {
        "type": "file",
        "description": "Path to arkts configuration file",
        "default": "$ORIGIN/arktsconfig.json"
    },
    "--ast-verifier": {
        "type": "group",
        "description": "Configure AST-verifier.",
        "default": "false",
        "sub": {
            "warnings": {
                "type": "list",
                "description": "Print warnings and continue compilation even if AST tree is incorrect.",
                "default": [],
                "values": ast_checks
            },
            "errors": {
                "type": "list",
                "description": "Print errors and aborts compilation if AST tree is incorrect.",
                "default": ["ArithmeticOperationValid", "CheckAbstractMethod", "CheckStructDeclaration", "EveryChildHasValidParent", "ForLoopCorrectlyInitialized", "GetterSetterValidation", "IdentifierHasVariable", "ModifierAccessValid", "NodeHasParent", "NodeHasType", "NoPrimitiveTypes", "ReferenceTypeAnnotationIsNull", "SequenceExpressionHasLastType", "VariableHasEnclosingScope", "VariableHasScope", "VariableNameIdentifierNameSame"],
                "values": ast_checks
            },
            "phases": {
                "type": "list",
                "description": "Specify phases to finalize with ASTVerifier.",
                "default": ["after"],
                "values": ["before","each","after"]
            },
            "full-program": {
                "type": "bool",
                "description": "Analyze full program, including program AST and it's dependencies.",
                "default": False,
            },
            "json": {
                "type": "bool",
                "description": "Report in json-format instead of stderr dump. More verbose.",
                "default": False
            },
            "json-path": {
                "type": "file",
                "description" : "Path to json-dump (if enabled). ",
                "default": "astverifier_report.json"
            }
        }
    },
    "--bco-compiler": {
        "type": "list",
        "description": "Bytecode optimizer's compiler arguments.",
        "default": [],
        "values": []
    },
    "--bco-optimizer": {
        "type": "list",
        "description": "Bytecode optimizer arguments.",
        "default": [],
        "values": []
    },
    "--debug-info": {
        "type": "bool",
        "description": "Compile with debug info.",
        "default": False
    },
    "--debugger-eval": {
        "type": "group",
        "description": "Compile given file in evaluation mode.",
        "default": False,
        "sub": {
            "line": {
                "type": "int",
                "description": "Line in the source file code where evaluate occurs.",
                "default": 0
            },
            "source": {
                "type": "file",
                "description": "Path to evaluation mode source file.",
                "default": ""
            },
            "panda-files": {
                "type": "file",
                "description": "Paths to evaluation mode (.abc) files, must be accessible.",
                "default": []
            }
        }
    },
    "--dumb-after-phases": {
        "type": "list",
        "description": "Generate program dump after running phases in the list.",
        "default": []
    },
    "--dumb-assembly": {
        "type": "bool",
        "description": "Dump pandasm.",
        "default": False
    },
    "--dumb-ast":{
        "type": "bool",
        "description": "Dump the parsed AST.",
        "default": False
    },
    "--dumb-ast-only-silent": {
        "type": "bool",
        "description": " Dump parsed AST with all dumpers available but don't print to stdout.",
        "default": False
    },
    "--dumb-before-phases": {
        "type": "list",
        "description": "Generate program dump before running phases in the list.",
        "default": []
    },
    "--dumb-cfg": {
        "type": "bool",
        "description": "Dump the constructed CFG into a .dot file.",
        "default": False
    },
    "--dumb-debug-info": {
        "type": "bool",
        "description": "Dump debug info.",
        "default": False,
    },
    "--dumb-dynamic-ast": {
        "type": "bool",
        "description": "Dump AST with synthetic nodes for dynamic languages.",
        "default": False
    },
    "--dumb-ets-src-after-phases": {
        "type": "list",
        "description": "Generate program dump as ets source code after running phases in the list.",
        "default": []
    },
    "--dumb-ets-src-before-phases": {
        "type": "list",
        "description": "Generate program dump as ets source code before running phases in the list.",
        "default": []
    },
    "--dumb-perf-metrics": {
        "type": "bool",
        "description": "Dump es2panda performance metrics.",
        "default": False
    },
    "--dumb-size-stat": {
        "type": "bool",
        "description": "Dump size statistics.",
        "default": False
    },
    "--emit-declaration": {
        "type": "bool",
        "description": "Emit declaration to .abc file.",
        "default": False
    },
    "--ets-module": {
        "type": "bool",
        "description": "Compile the input as ets-module.",
        "default": False
    },
    "--ets-path": {
        "type": "file",
        "description": "Legacy option to set global prefix path for all compiled modules.",
        "default": ""
    },
    "--ets-unnamed": {
        "type": "bool",
        "description": "Legacy option to compile a module as unnamed.",
        "default": False
    },
    "--ets-warnings": {
        "type": "bool",
        "description": "Enable ETS-warnings.",
        "default": False,
        "sub": {
            "werror": {
                "type": "bool",
                "description": "Treat all enabled warnings as errors.",
                "default": False
            },
            "enable": {
                "type": "list",
                "description": "Specify warnings to enable. Overrided by ':disable=' suboption.",
                "default": ["subset_aware", "subset_unaware"],
                "values": ets_checks
            },
            "disable": {
                "type": "list",
                "description": "Specify warnings to disable. Overrides ':enable=' suboption.",
                "default": [],
                "values": ets_checks
            },
        }
    },
    "--eval-mode": {
        "type": "enum",
        "description": "--eval-mode: (js-only) Set 'eval'-mode.",
        "default": "none",
        "values": ["none", "default", "direct", "function"]
    },
    "--exit-after-phase": {
        "type": "string",
        "description": "Exit compilation after running the provided phase.",
        "default": ""
    },
    "--exit-before-phase": {
        "type": "string",
        "description": "Exit compilation before running the provided phase.",
        "default": ""
    },
    "--extension": {
        "type": "enum",
        "description": "Parse the input as the given extension.",
        "default": "ets",
        "values": ["js", "ts", "as", "ets"],
    },
    "--gen-stdlib": {
        "type": "bool",
        "description": "Gen standard library.",
        "default": False
    },
    "--generate-decl": {
        "type": "bool",
        "description": "Input static file and generate static declaration files.",
        "default": False,
        "sub": {
            "enabled": {
                "type": "bool",
                "description": "Whether to enable static declaration file generation",
                "default": False
            },
            "path": {
                "type": "file",
                "description": "Output path for generated static declaration files.",
                "default": ""
            }
        }
    },
    "--help": {
        "type": "bool",
        "description": "Print this message and exit.",
        "default": False
    },
    "--list-files": {
        "type": "bool",
        "description": "Print names of files that are part of compilation.",
        "default": False
    },
    "--list-phases": {
        "type": "bool",
        "description": "Dump list of available phases.",
        "default": False
    },
    "--log-level": {
        "type": "enum",
        "description": "Log-level.",
        "default": "error",
        "values": ["debug", "info", "warning", "error", "fatal"]
    },
    "--module": {
        "type": "bool",
        "description": "Parse the input as module (JS only option).",
        "default": False
    },
    "--opt-level": {
        "type": "int",
        "description": "Compiler optimization level.",
        "default": 0
    },
    "--output": {
        "type": "file",
        "description": "Compiler binary output (.abc),",
        "default": ""
    },
    "--parse-jsdoc": {
        "type": "bool",
        "description": "Enable the ability to parse jsdoc.",
        "default": False
    },
    "--parse-only": {
        "type": "bool",
        "description": "Parse the input only.",
        "default": False
    },
    "--perm-arena": {
        "type": "bool",
        "description": "Place AST trees in permanent arena.",
        "default": False
    },
    "--plugins": {
        "type": "list",
        "description": "Plugins. ",
        "default": []
    },
    "--simultaneous": {
        "type": "bool",
        "description": "compile all the files to abc in once.",
        "default": False
    },
    "--skip-phases": {
        "type": "list",
        "description": "Phases to skip.",
        "default": []
    },
    "--stdlib": {
        "type": "file",
        "description": "Path to standard library.",
        "default": ""
    },
    "--thread":{
        "type": "int",
        "description": "Number of worker threads.",
        "default": 0
    },
    "--version": {
    "type": "bool",
    "description": "Print Ark version, file format version and min supported file format version"
    }
}
