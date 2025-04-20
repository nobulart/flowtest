using Test, HTTP, JSON3, FilePaths
include("/Users/craig/flowtest/app.jl")
@testset "Genie API" begin
response = HTTP.get("http://localhost:8000/hello")
@test response.status == 200
json_data = JSON3.read(response.body)
@test json_data.message == "Hello, World!"
response = HTTP.get("http://localhost:8000/data")
@test response.status == 200
if isfile("/Users/craig/flowtest/data.csv")
json_data = JSON3.read(response.body)
@test haskey(json_data, :columns)
@test length(json_data.columns) == 5
else
@test JSON3.read(response.body) == Dict("error" => "Dataset not found")
end
end