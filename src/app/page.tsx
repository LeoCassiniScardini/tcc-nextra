import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Nextra 4",
  description: "Nextra 4 is here.",
};

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center mt-20">
      <h1 className="text-center md:text-left text-[44px] ml-10 mt-10 m-0 font-bold max-w-200">          
        Documentação TCC
      </h1>
      <h2 className="text-center md:text-left text-[34px] ml-10 m-0 font-bold max-w-200">
        Juizado especial Civel
      </h2>

      <div className="text-left max-w-200 mt-10 mb-10 ml-10 m-0">
        <p className="mb-7">
            Este espaço foi criado para centralizar e organizar toda a documentação do TCC.
        </p>

        <p className="mb-7">
            Conteudo Tabalhado:
        </p>
        <p className="font-bold mt-2">Relacionado à direito:</p>
        <ul>
          <li>- Direito</li>
          <li>- Causas Processuais</li>
          <li>- Juizado Especial</li>
        </ul>

        <p className="font-bold mt-2">Relacionado à computação:</p>
        <ul>
          <li>- Ontologia</li>
          <li>- SABiO</li>
          <li>- OntoUML</li>
          <li>- UFO</li>
        </ul>

        <p className="mb-7 mt-10">
            Explore os conteúdos, utilize a busca para encontrar o que precisa!
        </p>
      </div>
    </div>
  );
}
