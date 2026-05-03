name := "pharma-bricks-spark"

version := "1.0"

scalaVersion := "2.12.17"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.4.1",
  "org.apache.spark" %% "spark-sql" % "3.4.1",
  "org.apache.spark" %% "spark-hive" % "3.4.1",
  "io.delta" %% "delta-core" % "2.4.0",
  "org.postgresql" % "postgresql" % "42.6.0",
  "org.json4s" %% "json4s-jackson" % "4.0.6"
)

// For local development
resolvers += "Delta Lake" at "https://dl.bintray.com/databricks/spark-maven"

// Main class configuration
Compile / mainClass := Some("Main")

// Assembly settings for creating fat JAR
assembly / assemblyMergeStrategy := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case PathList("reference.conf") => MergeStrategy.concat
  case _ => MergeStrategy.first
}

assembly / assemblyJarName := s"${name.value}-${version.value}.jar"
