using Genie, Genie.Renderer.Json, DataFrames, CSV, FilePaths
Genie.config.server_port = 8000
route("/hello") do
json(Dict("message" => "Hello, World!"))
end
route("/data") do
if isfile("/Users/craig/flowtest/data.csv")
df = CSV.read("/Users/craig/flowtest/data.csv", DataFrame)
json(first(df, 5))
else
json(Dict("error" => "Dataset not found"))
end
end
Genie.up()