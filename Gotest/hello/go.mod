module example.com/hello

go 1.22.2

replace example.com/greetings => ../greetings

require example.com/greetings v0.0.0-00010101000000-000000000000 // indirect
