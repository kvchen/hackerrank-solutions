languages = set("C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC".split(":"))

def main():
	num_entries = int(input())

	for i in range(num_entries):
		lang_id, lang = input().split()
		print("VALID") if lang in languages else print("INVALID")


if __name__ == "__main__":
	main()