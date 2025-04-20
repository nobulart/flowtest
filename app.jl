using Genie, Genie.Renderer.Json, DataFrames, CSV, FilePaths
route("/hello") do
json(Dict("message" => "Hello, World!"))
end
route("/data") do
if isfile("iris.csv")
df = CSV.read("iris.csv", DataFrame)
json(first(df, 5))
else
json(Dict("error" => "Dataset not found"))
end
end
start()