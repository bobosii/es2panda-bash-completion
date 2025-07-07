function es2panda(){
    echo("Author e-day")
}

_es2panda() {
    local cur prev out
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # Write your own path
    # Example /Users/emirhanday/Documents/es2panda-bash-completion/completion.py

    out="$(python3 /Users/emirhanday/Documents/es2panda-bash-completion/completion.py "${COMP_WORDS[@]}")"
    COMPREPLY=( $(compgen -W "${out}" -- "$cur") )

}
complete -F _es2panda es2panda

